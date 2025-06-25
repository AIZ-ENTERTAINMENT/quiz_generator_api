import asyncio
import os

from google import genai
from google.genai.types import (GenerateContentConfig, GoogleSearch,
                                ThinkingConfig, Tool)


class GeminiClient:
    """Gemini API 클라이언트 클래스"""

    _api_key = os.getenv("GEMINI_API_KEY", "AIzaSyD7njri5rYS6-J6KkGhxGPoR8aeov6CX0g")
    
    
    _model_id = "gemini-2.5-flash-preview-05-20"
    
    @classmethod
    def _create_client(cls):
        """새로운 Gemini 클라이언트 인스턴스 생성"""
        return genai.Client(
            api_key=cls._api_key,
        )
    
    @classmethod
    def _change_api_key(cls):
        if(cls._api_key[6] == "D"):
            cls._api_key = "AIzaSyBMfbos6335EAi_Kl7vacDwye6Cpr1W-nc"
        elif (cls._api_key[6] == "B"):
            cls._api_key = "AIzaSyAssN0SB3z6XWX7Ub0j6Zb5jhsVDzDcqE4"
        elif (cls._api_key[7] == "s"):
            cls._api_key = "AIzaSyABxsZKWHIhwsrmXi6SCND6s5uOT2vhBok"
        else :
            cls._api_key = "AIzaSyD7njri5rYS6-J6KkGhxGPoR8aeov6CX0g"
        print(f"Gemini API Key 변경 완료: {cls._api_key}")
    
    @classmethod
    async def generate_structured_content(cls, system_prompt, response_schema, contents, 
                                        max_output_tokens=100000, 
                                        thought=None, 
                                        thinking_budget=None,
                                        temperature=None, 
                                        top_p=None, 
                                        top_k=None,
                                        max_retries=4):
        """구조화된 콘텐츠 생성 (기존 gemini_structed 함수 대체)"""
        
        for attempt in range(max_retries):
            try:
                # 매번 새로운 클라이언트 생성
                client = cls._create_client()
                
                response = await client.aio.models.generate_content(
                    model=cls._model_id,
                    contents=contents,
                    config=GenerateContentConfig(
                        system_instruction=system_prompt,
                        max_output_tokens=max_output_tokens,
                        response_mime_type="application/json",
                        response_schema=response_schema,
                        thinking_config=ThinkingConfig(
                            include_thoughts=thought,
                            thinking_budget=thinking_budget
                        ),
                        temperature=temperature, 
                        top_p=top_p, 
                        top_k=top_k
                    )
                )
                return response
                
            except Exception as e:
                print(f"Gemini API 호출 중 에러 발생 (시도 {attempt + 1}/{max_retries}): {e}")
                
                if attempt == max_retries - 1:  # 마지막 시도
                    raise e
                
                if "429" in str(e):
                    cls._change_api_key()
                    
                # 연결 관련 에러인 경우 추가 대기
                if any(keyword in str(e).lower() for keyword in 
                       ['closed=True', 'runtimeerror', 'connection', 'transport']):
                    await asyncio.sleep(2 ** attempt)  # 지수 백오프
                else:
                    await asyncio.sleep(1)
    
    @classmethod
    def search_with_grounding(cls, system_prompt, contents, 
                            max_output_tokens=20000, 
                            thought=None, 
                            thinking_budget=None,
                            temperature=None, 
                            top_p=None, 
                            top_k=None,
                            max_retries=4):
        """웹 검색을 포함한 콘텐츠 생성 (기존 gemini_search 함수 대체)"""
        
        for attempt in range(max_retries):
            try:
                # 매번 새로운 클라이언트 생성
                client = cls._create_client()
                
                google_search_tool = Tool(
                    google_search=GoogleSearch()
                )

                response = client.models.generate_content(
                    model=cls._model_id,
                    contents=contents,
                    config=GenerateContentConfig(
                        system_instruction=system_prompt,
                        tools=[google_search_tool],
                        response_modalities=["TEXT"],
                        thinking_config=ThinkingConfig(
                            include_thoughts=thought,
                            thinking_budget=thinking_budget
                        ),
                        max_output_tokens=max_output_tokens,
                        temperature=temperature, 
                        top_p=top_p, 
                        top_k=top_k
                    )
                )

                contents = response.candidates[0].grounding_metadata.grounding_supports
                references = response.candidates[0].grounding_metadata.grounding_chunks
                search_queries = response.candidates[0].grounding_metadata.web_search_queries

                return contents, references, search_queries, response
                
            except Exception as e:
                print(f"Gemini 검색 API 호출 중 에러 발생 (시도 {attempt + 1}/{max_retries}): {e}")
                
                if attempt == max_retries - 1:  # 마지막 시도
                    raise e
                
                if "429" in str(e):
                    cls._change_api_key()
                    
                # 연결 관련 에러인 경우 추가 대기
                if any(keyword in str(e).lower() for keyword in 
                       ['closed=True', 'runtimeerror', 'connection', 'transport']):
                    import time
                    time.sleep(2 ** attempt)  # 동기 함수이므로 time.sleep 사용
                else:
                    import time
                    time.sleep(1)


# 기존 함수들을 클래스 메서드로 교체
async def gemini_structed(system_prompt, response_schema, contents, 
                    max_output_tokens=10000, 
                    thought=None, 
                    thinking_budget=None,
                    temperature=None, 
                    top_p=None, 
                    top_k=None):
    """기존 gemini_structed 함수의 래퍼"""
    return await GeminiClient.generate_structured_content(
        system_prompt=system_prompt,
        response_schema=response_schema,
        contents=contents,
        max_output_tokens=max_output_tokens,
        thought=thought,
        thinking_budget=thinking_budget,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k
    )

def gemini_search(system_prompt, contents, 
                  max_output_tokens=20000, 
                  thought=None, 
                  thinking_budget=None,
                  temperature=None, 
                  top_p=None, 
                  top_k=None):
    """기존 gemini_search 함수의 래퍼"""
    return GeminiClient.search_with_grounding(
        system_prompt=system_prompt,
        contents=contents,
        max_output_tokens=max_output_tokens,
        thought=thought,
        thinking_budget=thinking_budget,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k
    )

def model_dumps(contents:list):
    return [c.model_dump() for c in contents]

def calculate_gemini_cost(usage_metadata, search_queries:list=[], wd_rate=1400):
    if search_queries:
        search_api_cost = 35/1000
    else:
        search_api_cost = 0
    input_token_cost = usage_metadata.prompt_token_count * 0.15/1000000
    output_token_cost = usage_metadata.candidates_token_count * 3.5/1000000
    total_cost = (search_api_cost + input_token_cost + output_token_cost)*wd_rate
    return total_cost