

import ast
import asyncio
import random
from datetime import datetime, timedelta

from fastapi import HTTPException
from google.cloud import bigquery
from google.oauth2 import service_account

from app.libs.database import with_session
from app.libs.gemini_client import (calculate_gemini_cost, gemini_search,
                                    gemini_structed, model_dumps)
from app.libs.llm_parameter import (BEGINNER_TOPIC_CURATION_PROMPT,
                                    BEGINNER_TOPIC_CURATION_RESPONSE_FORMAT,
                                    GCP_ACCOUNT_CREDENTIALS, GCP_PROJECT_ID,
                                    GOOGLE_TREND_QUERY,
                                    KEYWORD_RECOMMENDATION_FORMAT,
                                    KEYWORD_RECOMMENDATION_PROMPT,
                                    TOPIC_CURATION_FORMAT,
                                    TOPIC_CURATION_PROMPT,
                                    TOPIC_SEARCH_INFO_PROMPT)
from app.models.topic_history import TopicHistoryORM
from app.route.topic.schema import TopicHistoryRequest


@with_session
async def create_topic_history(req: TopicHistoryRequest, session=None):
    "Create Topic History"
    try :
        return await TopicHistoryORM.create(
            topic=req.topic,
            sub_topic=req.sub_topic,
            related_topic=req.related_topic,
            difficulty=req.difficulty,
            session=session,
        )
    except :
        raise HTTPException(status_code=422, detail="Failed to create topic history")

@with_session
async def get_topic_history(topic_history_id: int, session=None):
    "Get Topic History"
    try :
        return await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    except :
        raise HTTPException(status_code=422, detail="Failed to get topic history")

@with_session
async def update_topic_history(topic_history_id: int, req: TopicHistoryRequest, session=None):
    "Update Topic History"
    topic_history = await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    if not topic_history:
        raise HTTPException(status_code=404, detail="Topic history not found")
    await topic_history.update_by_dict(
        data=req.model_dump(),
        session=session,
    )

@with_session
async def delete_topic_history(topic_history_id: int, session=None):
    "Delete Topic History"
    topic_history = await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    if not topic_history:
        raise HTTPException(status_code=404, detail="Topic history not found")
    await topic_history.delete(session=session)

@with_session
async def get_google_trend(session=None):
    "Get Google Trend"
    keyword_list = []
    for i in range(3):
        date = datetime.now() - timedelta(days=i+1)
        date = date.strftime("%Y-%m-%d")    
        trends_list = get_keywords_google_trends(date)
        if len(trends_list) > 0:
            break
    keyword_list = [[keyword["top_term"]] for keyword in trends_list]
    topic = random.choice(keyword_list)[0]
    return topic

def get_keywords_google_trends(date : str):
  credentials = service_account.Credentials.from_service_account_info(GCP_ACCOUNT_CREDENTIALS)
  client = bigquery.Client(project=GCP_PROJECT_ID, credentials=credentials)
  sql = GOOGLE_TREND_QUERY.format(date=date)
  job = client.query(sql)
  rows = job.result()
  records = [dict(row) for row in rows]
  return records

#challenger 퀴즈 생성 함수

def search_sub_topic(quiz_topic_search_info_system_prompt, topic, history_dict):

    contents, references, search_queries, response = gemini_search(quiz_topic_search_info_system_prompt, 
                                                            contents = topic,
                                                            max_output_tokens=100000, 
                                                            thought=False, 
                                                            thinking_budget=None)

    total_cost = calculate_gemini_cost(response.usage_metadata, search_queries)
    
    debug_contents = model_dumps(contents)
    debug_references = model_dumps(references)
    debug_search_queries = search_queries

    #검색 쿼리    
    input_queries = "\n".join([f"- {query}" for query in debug_search_queries])

    #검색 결과
    input_contents = "\n".join([f"- {c['segment']['text']} {c['grounding_chunk_indices']}" for c in debug_contents])
    
    #레퍼런스 사전
    references_dict = {f"{i}":r['web']['uri'] for i, r in enumerate(debug_references)}

    history_dict[topic] = {"input_queries": input_queries,
                            "input_contents": input_contents,
                            "references_dict": references_dict,
                            "cost": {"search": total_cost}}
    return history_dict

# 기존의 create_sub_topic_and_related_topic 함수
async def create_challenger_topic(topic : str):

    quiz_system_prompt = TOPIC_CURATION_PROMPT
    quiz_response_format = TOPIC_CURATION_FORMAT
    topic_system_prompt = KEYWORD_RECOMMENDATION_PROMPT
    topic_response_format = KEYWORD_RECOMMENDATION_FORMAT
    
    history_dict = search_sub_topic(TOPIC_SEARCH_INFO_PROMPT, topic, {})
    coroutines = []
    coroutines.append(create_sub_topic(quiz_system_prompt, quiz_response_format, topic, history_dict))
    coroutines.append(create_related_topic(topic_system_prompt, topic_response_format, topic, history_dict))
    
    sub_topic_result, related_topic_result = await asyncio.gather(*coroutines)

    quiz_content, sub_topic_titles, sub_topic_total_cost = sub_topic_result
    related_topics, related_topic_total_cost = related_topic_result
    
    history_dict[topic].update({
                           "sub_topic_jsons": quiz_content["quiz_groups"],
                           "sub_topic_titles": sub_topic_titles,
                           "related_topics": related_topics,}
                           )
    history_dict[topic]["cost"].update({"sub_topic": sub_topic_total_cost, "related_topics": related_topic_total_cost})
    
    challenger_history_dict = history_dict
    res = {
        "history_dict" : history_dict,
        "topic_history_list" : [[str(i+1), t] for i, t in enumerate(history_dict.keys())],
        "related_topics" : related_topics,
        "sub_topic_titles" : sub_topic_titles
    }   
    return res

async def create_sub_topic(quiz_system_prompt, quiz_response_format, topic, history_dict):
    
    METADATA_NAMES = {"reason": "퀴즈 생성 이유",
                "learning_objects": "퀴즈 목표", 
                "taxonomy": "카테고리/분류", 
                "seed_keywords": "연관 키워드",
                "difficulty_distribution": "퀴즈셋 난이도 설정"}
    
    user_msg = f"""
        **검색 쿼리**
        {history_dict[topic]["input_queries"]}

        **정보**
        {history_dict[topic]["input_contents"]}
        """
    response = await gemini_structed(quiz_system_prompt, 
                               ast.literal_eval(quiz_response_format), 
                               contents = user_msg, 
                               max_output_tokens=100000, 
                               thought=False, 
                               thinking_budget=None)
    
    sub_topic_titles = []
    quiz_content = ast.literal_eval(response.candidates[0].content.parts[0].text)
        
    for number, quiz_group in enumerate(quiz_content["quiz_groups"]):
        sub_topic_titles.append(quiz_group["quiz_group_title"])
        
        for i, quiz in enumerate(quiz_group["quiz_group"]):
            references = ", ".join([f"[{ref_num}]({history_dict[topic]['references_dict'][str(int(ref_num))]})" for ref_num in quiz["reference"].split(",")])
        
        for k, v in quiz_group["quiz_group_metadatas"].items():
            name = k
            if k in METADATA_NAMES:
                name = METADATA_NAMES[k]
        
    
    total_cost = calculate_gemini_cost(response.usage_metadata, search_queries=[])

    return quiz_content, sub_topic_titles, total_cost

async def create_related_topic(topic_system_prompt, topic_response_format, topic, history_dict):

    FIXED_TOPICS = ["🔍 실시간 구글 트렌드", "🎲 랜덤 주제"]
    
    input_queries = history_dict[topic]["input_queries"]
    input_contents = history_dict[topic]["input_contents"]
    
    user_msg = f"""
    {len(input_queries)}개의 검색 쿼리로 검색 완료**
    {input_queries}
    \n
    {len(input_contents)}개의 정보 추출 완료
    {input_contents}
    \n
    """
    
    response = await gemini_structed(topic_system_prompt,ast.literal_eval(topic_response_format), user_msg, max_output_tokens=5000, thought=False, thinking_budget=None)
    related_topic_content = ast.literal_eval(response.candidates[0].content.parts[0].text)
    related_topics = [[t["subject"]] for t in related_topic_content["related_subjects"]] + [[t] for t in FIXED_TOPICS]
    total_cost = calculate_gemini_cost(response.usage_metadata, search_queries=[])

    return related_topics, total_cost

#beginner 퀴즈 생성 함수

#기존 generate_begginer_topic 함수
async def create_beginner_topic(begginer_topic):
    
    response = await gemini_structed(
        system_prompt=BEGINNER_TOPIC_CURATION_PROMPT.format(quiz_group_title=begginer_topic),
        response_schema=ast.literal_eval(BEGINNER_TOPIC_CURATION_RESPONSE_FORMAT),
        contents="토픽 만들어줘",
    )
    
    history_dict = {}
    topic_curation_total_cost = calculate_gemini_cost(response.usage_metadata, search_queries=[])
    history_dict[begginer_topic] = response.parsed
    history_dict[begginer_topic]["cost"] = {"sub_topic": topic_curation_total_cost}
    
    begginer_history_dict = history_dict
    res = {
        # 백엔드에서 현재 미사용
        # "gemini_response" : response.parsed,
        "history_dict" : history_dict,
        # "topic_history_list" : [[str(i+1), t] for i, t in enumerate(history_dict.keys())],
        "checkbox_sub_topics" : [t["quiz_topic"] for t in response.parsed["topic_group"]]
    }
    return res
