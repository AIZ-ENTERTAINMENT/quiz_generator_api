
import ast

from app.libs.gemini_client import calculate_gemini_cost, gemini_structed
from app.libs.llm_parameter import (BEGINNER_QUIZ_FILTERING_RESPONSE_FORMAT,
                                    BEGINNER_QUIZ_FILTERING_SYSTEM_PROMPT,
                                    BEGINNER_QUIZ_GEN_RESPONSE_FORMAT,
                                    BEGINNER_QUIZ_GEN_SYSTEM_PROMPT,
                                    beginner_history_dict_preset)


async def create_beginner_quiz(beginner_quiz_topic):
    res = await generate_beginner_quiz(beginner_quiz_topic)
    return res

async def generate_beginner_quiz(beginner_quiz_topic):
    
    beginner_quiz_generator_history_dict = beginner_history_dict_preset

    response = await gemini_structed(BEGINNER_QUIZ_GEN_SYSTEM_PROMPT.format(quiz_group_title=beginner_quiz_topic), 
                                     ast.literal_eval(BEGINNER_QUIZ_GEN_RESPONSE_FORMAT), 
                                     "퀴즈 만들어줘", 
                                     max_output_tokens=100000)
    total_cost = calculate_gemini_cost(response.usage_metadata)
    beginner_quiz_generator_history_dict[beginner_quiz_topic] = {
                                                            "topic": beginner_quiz_topic, 
                                                            "sub_topic": beginner_quiz_topic,
                                                            # "quizs": response.parsed, 
                                                            "cost": {"quiz": total_cost}}

    res = {
        "gemini_response" : response.parsed,
        "history_dict" : beginner_quiz_generator_history_dict
    }
    return res

async def get_filtering_data(beginner_topic, beginner_quiz_raw_data, beginner_quiz_generator_history_dict):
    #beginner_quiz_raw_data는 generate_beginner_quiz 함수에서 response.parsed 값
    #history_dict는 generate_beginner_quiz 함수에서 history_dict 값
    
    beginner_quiz_filtering_system_prompt = BEGINNER_QUIZ_FILTERING_SYSTEM_PROMPT
    beginner_quiz_filtering_user_message = "퀴즈 전수 검사해줘"
    beginner_quiz_filtering_response_format = BEGINNER_QUIZ_FILTERING_RESPONSE_FORMAT
    
    category = beginner_quiz_raw_data["category"]
    subcategory = beginner_quiz_raw_data["subcategory"]
    quiz_group_title = beginner_quiz_raw_data["quiz_group_title"]
    quizs_categorymarkdown = f'## {category} > {subcategory}\n\n'
    i = 0
    quiz_df_ls = []
    for q in beginner_quiz_raw_data["quiz_group"]:
        quiz_df_ls.append({"Id": i, 
                           "Question": q['binary_choice_true_quiz']['quiz'], 
                           "Answer": "O", 
                           "IncorrectAnswer": "X"})
        i += 1

        quiz_df_ls.append({"Id": i, 
                           "Question": q['binary_choice_false_quiz']['quiz'], 
                           "Answer": "X", 
                           "IncorrectAnswer": "O"})
        i += 1

        quiz_df_ls.append({"Id": i, 
                           "Question": q['two_option_quiz']['quiz'], 
                           "Answer": q['two_option_quiz']["correct_answer"], 
                           "IncorrectAnswer": q['two_option_quiz']["nonsense_wrong_answer"]})
        i += 1

    beginner_quiz_filtering_data = []
    n=100
    for i in range(0, len(quiz_df_ls),n):
        system_prompt = beginner_quiz_filtering_system_prompt.format(quizs=str(quiz_df_ls[i:i+n]), quiz_group_title=quiz_group_title)
        response = await gemini_structed(system_prompt, 
                                         ast.literal_eval(beginner_quiz_filtering_response_format), 
                                         beginner_quiz_filtering_user_message, 
                                         max_output_tokens=100000)
        
        beginner_quiz_filtering_data += response.parsed["quiz_group"]
        beginner_quiz_generator_history_dict[beginner_topic]["cost"][f"filter_{i}"] = calculate_gemini_cost(response.usage_metadata)
    
    return beginner_quiz_filtering_data, quizs_categorymarkdown, beginner_quiz_generator_history_dict
