import os

beginner_history_dict_preset = {
    "history_dict":{
        "음식":{
            "topic_group":[
                {
                    "quiz_topic":"다양한 과일의 특징과 영양",
                    "number":1,
                    "quiz_data":"사과는 전 세계적으로 가장 흔하게 소비되는 과일 중 하나이며, 껍질째 먹을 수 있고 비타민 C와 식이섬유가 풍부하다.",
                    "two_option_quiz":{
                        "quiz":"껍질째 먹을 수 있고 비타민 C가 풍부한 흔한 과일은?",
                        "correct_answer":"사과",
                        "nonsense_wrong_answer":"사화"
                    },
                    "binary_choice_true_quiz":{
                        "quiz":"사과는 껍질째 섭취해도 무방한 과일이다.",
                        "correct_answer":True
                    },
                    "binary_choice_false_quiz":{
                        "quiz":"사과는 주로 동물성 단백질이 풍부하다.",
                        "correct_answer":False
                    }
                },
                {
                    "quiz_topic":"일상생활 속 채소의 종류와 효능",
                    "number":2,
                    "quiz_data":"당근은 주황색을 띠는 뿌리채소로, 베타카로틴이 풍부하여 체내에서 비타민 A로 전환되어 시력 보호에 도움을 준다.",
                    "two_option_quiz":{
                        "quiz":"베타카로틴이 풍부해 시력 보호에 좋은 주황색 뿌리채소는?",
                        "correct_answer":"당근",
                        "nonsense_wrong_answer":"당금"
                    },
                    "binary_choice_true_quiz":{
                        "quiz":"당근은 비타민 A의 전구체인 베타카로틴을 함유한다.",
                        "correct_answer":True
                    },
                    "binary_choice_false_quiz":{
                        "quiz":"당근은 주로 파란색 채소로 분류된다.",
                        "correct_answer":False
                    }
                },
                {
                    "quiz_topic":"필수 영양소를 품은 유제품의 세계",
                    "number":3,
                    "quiz_data":"우유는 칼슘과 단백질이 풍부하여 뼈 건강과 성장 발달에 필수적인 유제품이며, 다양한 형태로 가공되어 소비된다.",
                    "two_option_quiz":{
                        "quiz":"뼈 건강과 성장에 필수적인 칼슘과 단백질이 풍부한 유제품은?",
                        "correct_answer":"우유",
                        "nonsense_wrong_answer":"위유"
                    },
                    "binary_choice_true_quiz":{
                        "quiz":"우유는 뼈 건강에 좋은 칼슘을 많이 포함하고 있다.",
                        "correct_answer":True
                    },
                    "binary_choice_false_quiz":{
                        "quiz":"우유는 주로 비타민 C만으로 구성되어 있다.",
                        "correct_answer":False
                    }
                }
            ],
            "topic_group_title":"음식",
            "category":"Other",
            "subcategory":"식품",
            "cost":{
                "sub_topic":3.74731
            }
        }
    },
    "checkbox_sub_topics":[
        "다양한 과일의 특징과 영양",
        "일상생활 속 채소의 종류와 효능",
        "필수 영양소를 품은 유제품의 세계"
    ]
}
  
challenger_history_dict_preset = {
    "history_dict":{
        "음식":{
            "input_queries":"- 세계에서 가장 비싼 음식\n- 역사상 최초의 음식\n- 음식 관련 흥미로운 사실\n- 세계 각국의 특이한 음식 문화\n- 가장 오래된 음식 발견\n- 영양소에 대한 오해와 진실\n- 음식의 기원에 대한 재미있는 사실\n- 음식 관련 기네스 기록\n- 채소와 과일 구분\n- 세계 3대 진미\n- 고대 문명의 식생활\n- 향신료의 역사\n- 커피의 기원\n- 초콜릿의 역사와 유래\n- 꿀의 효능과 역사\n- 빵의 역사\n- 파스타의 기원\n- 쌀의 역사적 중요성\n- 김치의 기원\n- 치즈의 역사\n- 올리브 오일의 효능과 역사\n- 와인의 역사와 종류\n- 세계에서 가장 많이 소비되는 음식\n- 가장 매운 고추 품종\n- 신기한 채소 종류\n- 과일 속 씨앗의 역할\n- 식물성 단백질이 풍부한 식품\n- 설탕의 역사\n- 소금의 역사적 가치\n- 식중독 예방을 위한 식품 보관법",
            "input_contents":"- 떡볶이는 1953년 신당동 마복림 할머니가 짜장면 그릇에 가래떡을 떨어뜨린 실수에서 시작되었다. [0]\n- 쫄면은 1970년대 냉면 공장에서 직원이 사출 구멍을 잘못 맞춰 두꺼운 면발이 나온 실수로 탄생했다. [0, 1]\n- 감자튀김은 한 식당 손님이 감자튀김이 두껍다고 불평하자 요리사가 화가 나서 포크로 찍기 힘들 정도로 얇게 튀겨낸 것이 시초이다. [0, 1]\n- 도넛은 한 가정주부가 도넛을 튀길 때 가운데 부분이 잘 익지 않는 문제를 해결하기 위해 포크로 가운데를 뚫어 조리하면서 오늘날의 형태가 되었다. [0]\n- 두부는 며느리가 콩물을 데우다 시어머니가 오는 줄 알고 놀라 자리를 피한 뒤 돌아오니 콩물이 두부로 변해 있었다는 유래가 있다. [0, 2]\n- 와플은 1734년 영국의 한 요리사가 아내와 대화 중 고기를 두드리다 실수로 팬케이크에 구멍이 생기면서 탄생했다. [0]\n- 굴소스는 1888년 굴 요리 전문점 주인이 굴을 불에 올려놓고 잊어버려 진득한 소스로 졸아들어 개발되었다. [1]\n- 초콜릿 칩 쿠키는 1930년대 숙소 주인이 초콜릿 맛 쿠키를 만들고자 초콜릿 바를 잘게 부숴 반죽에 섞었으나 초콜릿 조각이 녹지 않고 그대로 남아 독특한 식감으로 탄생했다. [1]\n- 콘푸로스트는 1894년 윌 켈로그와 그의 형제가 환자 식단을 위해 곡물 실험 중 실수로 데친 밀을 방치하여 태우게 되었고, 굳어진 밀을 롤러에 넣어 조각내면서 만들어졌다. [1]\n- 마가린이 처음 나왔을 때는 구매자가 실제 버터와 혼동하지 않도록 밝은 분홍색이었다. [3]\n- 신선한 파인애플에는 단백질을 분해하는 효소가 들어 있어, 신선한 파인애플로 치킨 샐러드를 만들면 닭고기가 녹아 가루가 되기 시작한다. [3]\n- 일본 카레는 인도 카레가 아닌 영국 스튜를 모방하여 만들어졌다. [3]\n- 오렌지는 포멜로와 귤의 잡종이다. [3]\n- 케첩은 원래 멸치를 넣은 중국식 생선 소금물 소스였다. [3]\n- 크루아상은 진정한 프랑스 요리로 간주되지만 실제로는 오스트리아에서 유래했으며, 이슬람 초승달 모양은 오스트리아인이 오스만 제국의 적을 \"삼켰다\"는 의미를 담고 있다. [3]\n- 미국에서 마카로니 앤 치즈는 한때 고급 요리로 여겨졌다. [3]\n- 냉동 블루베리가 생 블루베리보다 항산화 성분(안토시아닌)이 더 많다. [4]\n- 설탕의 원료인 사탕수수는 약 8000년 전 남태평양 뉴기니에서 기원했으며, 약 2000년 전 인도에서 사탕수수 추출액으로부터 설탕 알갱이를 만드는 제조법이 발명되었다. [5, 6, 7, 8, 9]\n- 치즈의 역사는 선사 시대부터 시작되었으며, 동물의 내장에 담긴 젖이 내장의 레닛 성분에 의해 응고된 것을 우연히 발견하여 발전했을 것으로 추정된다. [10, 11, 12, 13]\n- 와인은 인류 역사상 가장 오랜 역사를 가진 술 중 하나로, 약 7000~8000년 전 메소포타미아 지역에서 처음 제조된 흔적이 발견되었다. [14, 15, 16, 17, 18]\n- 김치라는 이름은 원래 '지(漬)'나 '저(菹)'라고 부르다가 조선 초기에 '딤채'로 변했고, 음운 변화를 거쳐 '김치'가 되었다. [19, 20, 21, 22]\n- 오늘날 붉은 배추김치의 형태는 아메리카 대륙에서 유래한 고추가 포르투갈 상인을 통해 동아시아로 전해진 이후 나타났다. [20, 23]\n- 커피를 마시는 문화는 11세기에 커피의 원산지인 에티오피아로부터 아라비아로 처음 수출되면서 시작되었다. [24, 25, 26, 27, 28]\n- 초콜릿의 원료인 카카오는 아메리카 대륙의 열대 지방이 원산지이며, 약 3000년 전 고대 멕시코의 올메크족이 카카오 원두를 갈아 물에 탄 음료 형태로 마신 것이 초콜릿의 기원이다. [29, 30, 31, 32, 33]\n- 아즈텍 문명에서 카카오 원두는 음식이나 음료의 원료일 뿐만 아니라 화폐로도 쓰였으며, 100개의 카카오 원두로 노예 한 명을 살 수 있었다. [30, 33]\n- 포크는 10세기까지는 신분을 막론하고 손을 사용해 음식을 먹었으나, 프랑스 혁명을 거쳐 서민들의 일상에서 보편화되었다. [34]\n- 냉장고의 발명은 음식의 신선도를 유지하여 시간과 거리의 한계를 초월하게 되었으며, 세계적으로 식품 무역 시장 활성화에 큰 역할을 했다. [34]\n- 돼지는 우리나라 토종 가축이 아니며, '양돈'이라는 말의 '양'은 서양을 뜻하고, 삼겹살을 구워 먹는 문화는 1980년대 후반부터 보편화되었다. [2]\n- 자장면은 중국 음식이 아닌, 사실 우리나라에서 시작된 음식이다. [2]\n- 초기 인류의 음식은 수렵과 채집, 사냥이었으며, 농경은 온화한 기후의 강가 주변에서 밀 재배와 가축 사육으로 시작되었다. [35]\n- 고대 바빌로니아의 길가메시 서사시에는 목수들이 화이트 와인과 레드 와인을 마시면서 7일 만에 배를 건조했다는 기록이 있으며, 함무라비 법전에는 \"주벽이 나쁜 자에게는 와인을 팔아서는 안 된다\"는 규정이 있었다. [17]\n- 식물학적으로 과일은 식물의 꽃에서 발달한 씨앗을 포함한 부분을 의미하며, 채소는 식물의 뿌리, 잎, 줄기 등 과일 외의 다른 식용 가능한 부분을 의미한다. [36, 37, 38, 39]\n- 요리나 식품 분류에서는 보통 단맛이 나는 식물성 식품을 과일로, 덜 단맛이 나는 것을 채소로 간주한다. [36]\n- 딸기, 토마토, 수박, 참외 등은 식물학적으로는 과일에 속하지만, 요리에서는 채소로 간주될 수 있다. [36, 38, 40]\n- 고추와 방울토마토는 한해살이 식물에서 자라므로 생물학적으로 채소로 분류된다. [37]\n- 수박과 참외는 덩굴식물로서 한해살이 식물에서 열리기 때문에 생물학적으로 채소에 속한다. [37]\n- 식중독 예방의 3대 원칙은 청결(손 씻기, 위생적 취급), 신속(바로 섭취, 오랫동안 보관 금지), 냉각 또는 가열(5℃ 이하 또는 60℃ 이상 보관, 75℃ 이상 가열)이다. [41]\n- 육류는 공기와의 접촉을 차단하고 덩어리 고기로 보관하거나 공기가 통하지 않는 비닐랩 등으로 겹겹이 싸서 냉동 보관하면 1주일 이상 보관할 수 있다. [42]\n- 가금류는 핏물을 최대한 제거하고 밀폐하여 냉장 보관해야 한다. [42]\n- 조리된 음식은 실온에 방치하면 위해 미생물이 증식할 수 있으므로 가능한 한 빨리 섭취해야 한다. [41, 43]\n- 조리된 식품을 4~5시간 이상 보관할 경우, 반드시 60℃ 이상이나 10℃ 이하에서 저장하여야 한다. [41]\n- 냉장 보관 중에도 위해 미생물의 증식이 가능하므로, 저장했던 조리식품을 섭취할 때는 70℃ 이상의 온도에서 3분 이상 재가열해야 한다. [41]\n- 오염된 식품이나 기구와의 교차오염을 방지하기 위해 채소, 어류, 육류는 도마와 칼을 별도로 지정하여 사용해야 한다. [44]\n- 조리를 위해 냉동고에서 꺼낸 재료는 냉장실이나 찬물에서 해동하는 것을 권장하며, 해동된 식품은 실온에 방치하지 않고 바로 조리해야 한다. [44, 45]\n- 냉장고 용량의 70% 이내로 식품을 채워 냉기가 잘 순환되도록 하고, 한 달에 한 번 이상 청소하여 청결한 상태를 유지해야 한다. [45]",
            "references_dict":{
                "0":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYd-z02lcikoLbEiS-zTjmO2vMuUVcHmwRL1SKh-wE60Ev3hVqIsy5V0OOe0D77j6Sh6Fia30zDdmlxW1xhZUAnwWYwTmLBi9w221GGumPHl9LevkXQsWm4Oqppzr4YtUMlrGU",
                "1":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjlMxz70vAaCOU-uFBketoq0BvBYzRyWiI1MQNh-c3ufgCvCvUVF6Wv8KBxRYykJYBuUgnEMD4WsETup2uxgfrte5WdzWLQCB1yrk7HFg2HUI-1PxpI1GFKtZKdicyil3GR2BZfGR0YQ==",
                "2":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4s10IFrv6Fu35lpmrKIVbVCn8-5Hb47hnhMnJ_hVyHsdUivjt2qpZFmRgQvfgoQSN4UVugWu1-BZ2RIayyGKDjBX2mp0vBLFodaHoKV7TxnzcJGbtN5P71I1hnv20l7RhjxmUS_m9ZceDFg3PZGMOWOY=",
                "3":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE6ri51lgEIqRY6XkwuniuTKfuG3Ut-xvSTRoRZXM9_0hj2Vz-ybLLDkigvqrNgPvIoCWhuz8pJapsNdNKseid0Xfef1FqBKjW83IyQvCnoahLf-jYLZK4vn-_beP4H1kVEcQMZiBw4pBb7Ic0_xqEffzu",
                "4":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH08Ig0YYNYTbOwAN-CbKF2alRmsHhL_NLYb8Wk4XQeQpURWdw2n0s50ChbmczTYgiFCLE259OZYJqDsTIE61ZUOU3yCaE3wzZAvvYprCvB5g565T5udM-Es-EpL9yt-9D1OGt7HVHIBaaSvohXBP6t6c9DsG1CVKXSyz9MldC5r6Yhg7R2MyaUBHkrjMFl-jz0Tw9n5jYNnffFDbHmt5IiOYbvLESG38qyQm4gtNRHv93wklJzkqApUMnFwpW9FOt23GmA2h7YsjzL9VW9_kppRC70UfRRD_u7mOlaMmM=",
                "5":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwq4ND7QqKI809TP2c_ZhCdbeA-Vui7Y7cN_eKerFRQfrbexRBLuUvdl9XdjRz7dl-kZshE3qezNcuXbNGS_iM8Cv4BLSRehBB1ANu3Qyj_AIusq4MrqrkkTdSaD1xjWann87eZtUSqsAcbZgAptXd6ENz8Us2CtLnqMhFpJwVM7OEKVQCqQ==",
                "6":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBgWX-LSf11SAiK9ZFkC-piNuPbPlFHc8lTPy_F9JZ2qLv_a3dEzNldDU-6tBhfyraXh7hXldBo86ugK2kYbu2GlO2Po13SemQgqaVdEJp3tqdOVO5pIUT5wOqfSRrb_FzbiLHJlgMR_QWxnrL",
                "7":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_sFXzN3mopOcwEqhWnR7sgG3Wb5JGWcHJfACdhHyZZ28bVVf8oR9vtoayp9gTrnxOfzU2Duom2TY5FniLdCLiggVFXE5G-Ks62aF6wWgiukV3-90TaiPU4d1yCSubLQAMd6ysnPXpv8gy58KXdy34aUs=",
                "8":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUXd4hQoXx3TVKZPIo5mljAq1r3fkpHHQpjNwsiJVtVrpcrzG_PhRfpFc5azW1j769gJ86C3H63ba6_TCudfXlhEwPNGHdVXo4oG4yMYrBuxyu8i3X__5kd7U8OAfWUXfu4B4Qodc=",
                "9":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPi6JEMGrl-j8TrYyd8W4wJzRBd1h7EJ0paD4_UHVAT5KC8x3NK9zSNqkG7QvjOuC6AE3OmjSEe4iGp9Lk_vHdCxb2qXY5PTmFmJ--BKCdp-EbVmbKrbig9ckNibgq_kOMJf6kMW9Pog==",
                "10":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7Vg0n4rCi4YVd6rd85dv0gX6paR5MhlBNLOKQAup37Xk6Dnq9F8cwX22qlUVV54njX6bVXWdFWBfv_O9iKtLvEJXClnuTihlaIGUKZNe8TT-90hRA6ou6is1HmMU5U0B-CDyYbKB0aPYd",
                "11":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEANlQJfkaCpMsA6cvwjUiTaqPwLUd8zHbveaClD489LZDdkXijdmPlnVAF3tYwBwnl_VGzXWxC39kH67XORwBNT04PJ639iQ5tSLJ77c6InW9TjwfLCn5Agp1OXMADSCA=",
                "12":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExP-dkLHVA_JAfBzI7DC1JMBTBovY4aYXG_8gE3GGZ8tzS02EK7xDjXzltaVb9_9sc43z1HeGI2UDuDkiEsXybouOj_JfwK7fmWC9soS9Zk9DHiMZbUCWlc1E=",
                "13":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmhpmbtKTQlTREaOoGo3htMFT4PqDLZWhjOzVY_oD5oOP-XTCh_rW_3cclsCao-3qdCG4xJlOQqDGqVCrx6KrHozeZIIN6awTTd2fB_PeClpFEzg88t__fnWFlkixUXqLjm3stRlhBDjSTE4Iv3jAVnc2Mn1UuaMjj51ag8NT2AuDzkJ1mov-nGIgHB3KdSADHUYWi75n8o-JLSVYxByD46uh-CU45ynyCtQ==",
                "14":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtA2eSyg4W5HfIVzrvTGZXWSqMWEmTAALydFm2ML9I2oSm0q397ZqEfZWM7-xY3toDxbq2pRhKwGLrXmHRJx1EgsXSiqP8_Xk7B3WRZI9qMf5gZU7pNec3VHkbAGi3NcyvEvdqBUDpN40F3AKd62Oy",
                "15":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSptxut9dSMeG3wuvMsNr66wJvkRmzaU5w-gct62dUZrmsV543fQnEnRlUwVi2jwAVrbhI7-pOGDndDIbPnDoBWs-KQtgxgcX4A63iRvyo6WKvAZShAAQqER8AqEnu5y4IF7xGHckexY1gHVqEmXzPEGw9mFwSlFHsAxvUXspygA==",
                "16":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQY-wxPNC9rQG-JDxZbwGasI4uadEZyMHF5t5sBSbs9FEtvCzM56yS5oJdy4wHRCFF0zYmB_J2ftRLM6CB_yB40l6cIJVVA39COKnUhJ_pCqRO_aHdSKMWMTspTzjUTtDTPJIJ8NQnUMQLLwnU1LlhGzv3UbGx8IxQbGn_kR0=",
                "17":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0svwWasa2e-Z8mELCa8cR37kIprV1k-kaqtGz1KYNdmQZrP3cQAKrN2Y3Rlg21LtSph5wpnOXXUEylunk_Lhyr5u5rjBZQFDvbDxLYMaIeXnFGxIvZHeoQvniV4QMYZac4aZEJ9H-ZrnJZMaIQOZOFFWAbQeapXqsnc3cxDlZNy3cPdA_F5w4hC5uPdArQUGRlBteBKzzMjZFuWtydDdlIgQGKlmeSJPtXbglEgP703aS8Gd129pd0WUJNwRQalMz5KCBrkX3tAwSTe-GpobWvLbeHo1l1XEvZfOM5Al6TkgReWr0hWkIwsgWatOmHQKvwyUaN3oL9zncRC3tjrMaj2EAS25E-hfYS2HYHVFxfWlEOWojPcrTT7TcTEFTOrOuophi9ZcYY-mYetcebDEHG6d1LMwciBviNrR4UJtaFDDBO66DmTITT_b-0zA=",
                "18":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQudmbTmGHNo5yLIbnbMqj1N8s35jolgAt8OqKrbWsPxkm1F4MqGMBr9BnrZwEU3c7xW4tjDSMB36CI3nU_qEoXU5mVhoLRjofBaF-OZgBvmuP79xkbg==",
                "19":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdtOsr-WdaZVwGOrgQvyGb0SvB6vogk1flViTCAofceVa1zuXiEjKKkVUOyQCFeWGM7njyWuoc4rDP2MFHl7t3B3KGOzmGaDqsX5kugSY0PXNBToTF6RgnOhjngAsvoCArRO0vlLE=",
                "20":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1vfAP_ACJ02uNLeAZ72MbkNFEFoFuB6NYd3cWKhnjp5n7WjcCAj9pD8rTd7Gxnp-4UPRfWO3xZwpiz8Hc3JDll2GVLCRlfKytKLZ5OEPwTbbnYp0P5h0619fImiHuc3w=",
                "21":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPEpEF-rYHsNrd9qyw2WFDmBksHe87SwJ5u2AbQ62Gotlft8iyvsEMfJC5jK6yR1FzVUCHUmpHMBRWPH2_bafdWn7-O0FeN0xBMZioyh7mfMu_Md4DohRimRH9Fi7da8UecU1tcaHLZ3wXe7l5jZ4rEwqD1Zt9ZvvhYxHmrSH3P1ntbEiFmDz6hMBCLWZmaXgFMr98vEdBoJ3W8Jt10a7RQc_94ZX_pBRCb-Mwxm0s3b52uAlUEyxPJ1KS2jfn",
                "22":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY_LufWS3xTR0EFu0wN5D56kOlCuOU4ylVOUNs1TX7hzHn21Z2JXhHd1Bkpjn85NKWl8rJNC9er6girDS_o7-B5u3EPuAktarwy5ajN_CPmQO1heOkn5C3W2m3EoV6QoDpvH6wgJWfFoIhUeVUZ2EfX9xDBomW2t1wjs6pLkgIvVC78W0r2YUxkreJPQ==",
                "23":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmljiT7ZyWEtBx88FmiKBB-To6uhVwnHo_5rAUlZJBbWeFG2gXieKu0ItXM_mM34psIngTS_jgEm6wUfWO22gGrNt-cXJb91VLT0qjLxMukK_ut2y8WFIqsjfDIe_-ym2aDzILtgBi5tA8YUZrfKpcZnowPpzOUUWLsoaM",
                "24":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrFx0y6Cp5DkhzAbvjWEQFzvdrc4fdxO9eoRJQkMf6hvomQmoy4TDnWnqW7Fj6j7o7mxiysWSeRn4t0YFYiNoOvGBbxaZgUMUdlNoIcMWTbbGWOMVDKizQP1zfCdkszLa3CMUerRoj4o_vwuZxt4Q=",
                "25":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPZBgPOFP5oSkdDnXE6lEQbEet0lUZuGcWVGWQx9t7SDxVpPt_thJXzw62tiwmA4fMnXHcikgYj1dq9j_fLmxxLtcsI1k6d2V-iuWHTUpNXhHPwHaj_4hNuRwIeRiVyms_kbkFsHW8JEy33uRYqQ==",
                "26":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7-m90gIjFrEl1Vb7vY5MoDq1LSokeZunBC_IBVK4Q7_9VCJw5xVGQCVRfhxpBWCud-bF12swO3BZRC_JpmmabFvZ5XN6EZ-taqpcBX3yoVYkgPxyDKz--judMuDU=",
                "27":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIa4iPz5mMyc777w_98nFmDwf_GPM8Ms2JOltbFU84AzwnWNf72SqqnUQ2xfUaFQFcRDaJvT47_TaG0-ciHYCo3ZOzViPx9IFeQaU3N8p3vGvXBefoNbEhs3y-3zeCmjZSCRLLBUQ8Zfo=",
                "28":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGex8rbDGmjKt45fpAuzdkLN20b85akuFGNHp68lp2EgA0_TfyMEleJ585-4zDOGM33tcyEa4jrY5bhUXx9w2iE2ahMrZRpd_Oxmhj2AhSvSfrBHs4BxpnUxbUMbzMXK9_9NZKdnWpT9gX_Xm57AZU-ij5p6J2F0bfVTLQz5UrktHEYxuq1ig==",
                "29":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbVxHks12wQCLjit9k_b6jtk8Kz1K_JeK8ypZMHAsCgxN3Dg2FhDADZV_I9Wtcoe6XMFnJGW6PwjZafxtaCIDHy0htFgAjUF6R-b2CWmpvF_pJQy7p82Au5IQiAcECv3soHMi55NBIPBUj0c_mVY35D8vZWk5ViANBWGT3m37ELLc_7eayoLT_o2qNKXFlKA==",
                "30":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOcg6veLIWMreppYCEwSkyVwnByBz5IUOcLy8I_JXTYAMGBCh8FBwMfzKn2nvX_EVRxUysGDuLC7jWQfG1I14-CZ0RHXOhou_IAw_qrIijcWIwQ4cSH3CClsII9gKAmQw0j2zz0hqf0p5YEVo=",
                "31":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTzRW0k3f1b7yyybvaN8p6ZRW58I3kHKrqFDeryErqhIDhUbhvJyKUTGvmdcEqqiRbb3OAic4D2mCTfUjUET-I2dUVr7OS8PDhxvzgu3w5hDrRgswpmqXU0vAo",
                "32":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG1_WcRCPhI9TUfQ1-po2TxRmuT9nOvsrDHEa9pkq5mJLDmU3Xy3KscixMNQHqgPLGIswl2oMsSGC_y2YcJlvGC7chlzwP6_63CnDuZv7lb370JQu7Wpoh78uvdCiykepTQtL7QflMyOKIzgm28lQzSzGkVxo0",
                "33":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiGjOC88Hd1SPIF8xWph8MLUwsYadpUhSAlSZRwFSX0JO_f7EhTCuR-WJjz-2iVbtKnpRa8F1cgHc27SRCI_OmCmI_LzwtSOL8vkmGG7Fn1zhnYRV3acOV48xx-RhCM9QoaRXkmKOz",
                "34":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIrQaQV1zgiN5UDZlPKje0clXV_RHgV9XXU54Im-iyd42-mBYjUtFpgsLiJZqxmdfbcZx-YU_HKGSBIA6thgtzdkCoxOwHjV6sh_698wn0Clm7bA_vcpcE6dfS01-8lwhIYrZ0eHjanTQq5pT8s7PTxNcF7i51qloyPp0sMCIZ8lYuaxYoBTJN2t-WtH8rQpZ1VZSqpyJarZcoE0Y1Cn5tE3SSaobYQJsoO0J3HIdfKXPnylyjyWTS3zIbFw8BQirJGQdd-qOpLHJTmoNqwd2X82gay2wO-tOzukpdpYxAae7gbaA=",
                "35":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSUxub0_k7Zlp5Y5n4b-Q5rulA4B8kzpZjKqDAed1k37vNu8CEIqCQqVhqvgYx-U6x3CFjZT_fWsKwDMIUtWWfHfxq-7i9Rksk2RFWTb6qDMhHviLwyA==",
                "36":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1DoTEfhYs1VLxLufoFNk4xa5aaz5r-XSh30Z9Z9OAndf9UwJhpFBqnRpDgpJAv_jpymBOGfv-09mv1dkMx8JRsLLv0MTwe7eDEkluThcOsfQayk1PXeqQRQJj2w==",
                "37":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnF2LuYMuagK1YORlQJFcNeS0AOVvYnMloGIpYpxrL6IDcqdEW4eTIcmKmHytm9Hyr7gf3dq3Nnli0kNtt5rzorkCx9dDHk0wS8AFMLD6VsXQtcDuNBKpi5MX4QU6qH2Mj",
                "38":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvw0_1JnTDjix7jy-KR6u0l6RPgmAmokwPariKxqfCryQKalxAE8JVCde7Nx_p5S1CmIfo1Q3K4MCbzqx7h2_FAvDvfzPiry2sAKPBtvlXQIX0NsNx7BBu9g0k5j8=",
                "39":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ZlLvwx7FLqoMj0uYAuXm6urIYy6VwftQ2rAzCAChmo8uikFeoGuGdHOk06ZRFs1SnrtcY4vja7NSDkvhDgpoTRKtZ-dvJFSlm3MG11u2oSiUFmtTX7o=",
                "40":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhUhezyLIM2ppGJVJQgewaxKtvk0ybku8D6JezEcRev32c6Rse5T0_BCPEHcSrVgylH1UBN3Y6WXxOb2N-QCBD5q6sUnRxiWv6bgonK6-bXpbRu04JcMIiPRVT4SBsi7IKrPpGFo1udkwdV6IzK_ocZS_yhWfqAPsSI6HmbMH51gb0M60iueqqzyqbT4PsfU8C76fTQv7IPW6JkvmoV-jlmIoqZA==",
                "41":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6RYAAMTBm2XH-BzoIWF_TAjFs47nCUzLXvhFRaOQY0npkLszpZAyL5YTTuFgkJ7wyMM9epq4wtHhKmFQz8-OK6GW_r1f3vYa-v2olnr5_EYc6VfzUWwuK3N617g_Alk=",
                "42":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_LFuGPwKdj9mDbFmAjg76E8lnnejIiEbRFv-ozR18TV7XEN5fChw44Obg_5xXo53NLB_VstofZdvxyHVkmDs38lrm2Z1xglnHoJT9QRzSxNXBMzL0N4Y8OimvfoVtZFTpSoj-8fw7R-DtzXLRKgI0JRGURA==",
                "43":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbTlr0KaEoYiX4oqX_X7gbpMM8k34ltJ9drdjOjclwxNrnx-6s9CfMSNWYfbPbAOdJ9q2iVOd7GAYxW152LcRxm0Zi9ZLl9AH1p0IoSlpIlzkiczbPCcEQma4aBKs_EPaM0KvP5atQ-4E8TqPYiEYixAEoOIemSCAK7WEag8lonqGSAyf0EdVvSm9FVAV9vctQHMjMuCorlRe7Nc3qmuC9wUzIEmzURkPKm4ofOjyI5SewI_BZeJIs4NCurPQYCsKXQSz0OdRhdLdro_hYWRkml3tPqvmYfk2heBH7zxhTokeZd-9IJ7QBK9r-K1kLx1rFWWx_Ikb91Pw4QRFecs3TWNA-CA6BlwpPgiHVReaVGcCF1FdqPWz_2sGfel1EM4fUKQ==",
                "44":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU9b4TwXNxEFACzFgViC5Hzn9xOqiF0BR9hbyw23CnLotxqw_0DvNaR65VuP9nUZW8Xbbko9jsNzSqqNIGa8I2S_AorGsc-u2XaUZ5RqFMShJHKBYKvaCExrVB4i-aZusoIuLTvZ0jL8aied5ALTLG219R30uMydfqnHuSlBr7P6MbsjlBzQZN-7ueWdbP4B6Hvl46kD0BQ93R",
                "45":"https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhWIbT3xKQzOlvdsGknnBiFmyLhodxOKT-GDrGnotMq-Ho5Kvzt4xe0PqqMeI5VU-zBHPiV575pVny_Js7DqmuZ371vf8hdABrh3ZxxZkdwNYfzdAMmFs7nwf2Je1Gf9ycp6pN7g=="
            },
            "cost":{
                "search":60.81579,
                "sub_topic":15.177610000000001,
                "related_topics":1.2653899999999998
            },
            "sub_topic_jsons":[
                {
                    "quiz_group_title":"음식에 얽힌 재미있는 탄생 비화",
                    "quiz_group_metadatas":{
                        "reason":"이 퀴즈 그룹은 우리가 매일 접하는 익숙한 음식들이 우연한 실수나 특별한 계기로 탄생했다는 흥미로운 사실을 중심으로 구성되었습니다. 학습자들이 음식의 기원에 대한 호기심을 자극하고, 예상치 못한 발견이 일상생활에 미치는 영향을 이해하도록 돕습니다.",
                        "learning_objects":"음식의 탄생 비화, 우연한 발견의 중요성, 일상 속 음식의 역사적 배경",
                        "taxonomy":"식품, 음식 역사, 기원, 재미있는 사실, 상식",
                        "seed_keywords":"음식 기원, 탄생 비화, 우연한 발견, 떡볶이, 쫄면, 감자튀김, 도넛, 콘푸로스트, 음식 역사, 식문화",
                        "difficulty_distribution":"easy: 60%, medium: 30%, hard: 10%"
                    },
                    "quiz_group":[
                        {
                            "quiz":"현재 우리가 즐겨 먹는 떡볶이가 처음 탄생하게 된 계기는 무엇일까?",
                            "correct_answer":"짜장면 그릇에 가래떡이 떨어진 실수",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"떡을 삶다가 우연히 양념이 섞인 사건"
                                },
                                {
                                    "wrong_answer":"쌀가루 반죽을 잘못 만들어서"
                                },
                                {
                                    "wrong_answer":"떡을 보관하다가 우연히 발효된 현상"
                                }
                            ],
                            "reference":"0"
                        },
                        {
                            "quiz":"면발이 쫄깃한 맛이 특징인 쫄면은 어떻게 만들어지게 되었을까?",
                            "correct_answer":"냉면 공장에서 면을 뽑는 기계 구멍이 잘못 맞춰져서",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"새로운 면 요리를 개발하려다"
                                },
                                {
                                    "wrong_answer":"밀가루 반죽을 잘못 숙성시켜서"
                                },
                                {
                                    "wrong_answer":"뜨거운 물에 면을 넣다가 실수로"
                                }
                            ],
                            "reference":"0, 1"
                        },
                        {
                            "quiz":"바삭하고 얇은 감자튀김이 처음 만들어진 재밌는 계기는?",
                            "correct_answer":"손님의 불평에 화가 난 요리사가 얇게 튀겨서",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"새로운 감자 요리법을 찾던 중"
                                },
                                {
                                    "wrong_answer":"감자를 튀기다가 기름 온도를 잘못 맞춰서"
                                },
                                {
                                    "wrong_answer":"감자 껍질을 벗기다 실수로"
                                }
                            ],
                            "reference":"0, 1"
                        },
                        {
                            "quiz":"가운데 구멍이 뚫려 있는 도넛의 독특한 모양은 어떻게 탄생했을까?",
                            "correct_answer":"도넛 안쪽이 잘 익지 않아서 포크로 구멍을 뚫어서",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"도넛을 더 예쁘게 만들려고"
                                },
                                {
                                    "wrong_answer":"도넛을 옮기기 편하게 하려고"
                                },
                                {
                                    "wrong_answer":"실수로 반죽에 구멍이 생겨서"
                                }
                            ],
                            "reference":"0"
                        },
                        {
                            "quiz":"아침 식사로 인기가 많은 콘푸로스트는 어떤 과정을 통해 만들어졌을까?",
                            "correct_answer":"환자 식단용 곡물 실험 중 밀을 태우고 굳은 것을 부수면서",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"맛있는 아침 식사를 만들려고"
                                },
                                {
                                    "wrong_answer":"곡물을 갈아서 반죽하다가"
                                },
                                {
                                    "wrong_answer":"곡물을 건조기에 넣다가 실수로"
                                }
                            ],
                            "reference":"1"
                        }
                    ]
                },
                {
                    "quiz_group_title":"세계 음식 문화와 역사 이야기",
                    "quiz_group_metadatas":{
                        "reason":"이 퀴즈 그룹은 전 세계 다양한 음식들의 역사적 배경과 문화적 특징을 다룹니다. 음식의 유래, 변화, 그리고 문화적 의미를 학습함으로써, 학습자들이 음식에 대한 이해를 넓히고 글로벌 식문화에 대한 흥미를 유발합니다.",
                        "learning_objects":"세계 음식의 역사, 문화적 배경, 음식의 변화 과정, 특정 식품의 유래, 글로벌 식문화 이해",
                        "taxonomy":"식품, 세계 문화, 역사, 기원, 지역 특색, 지리",
                        "seed_keywords":"음식 역사, 세계 음식, 문화, 마가린, 크루아상, 설탕, 초콜릿, 김치, 식재료, 유래, 식문화",
                        "difficulty_distribution":"easy: 70%, medium: 20%, hard: 10%"
                    },
                    "quiz_group":[
                        {
                            "quiz":"마가린이 처음 출시되었을 때, 버터와 헷갈리지 않도록 어떤 특징이 있었을까?",
                            "correct_answer":"밝은 분홍색이었다",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"독특한 모양으로 포장되었다"
                                },
                                {
                                    "wrong_answer":"일반 버터보다 훨씬 짰다"
                                },
                                {
                                    "wrong_answer":"특별한 향이 첨가되었다"
                                }
                            ],
                            "reference":"3"
                        },
                        {
                            "quiz":"프랑스의 대표적인 빵으로 알려진 크루아상의 실제 탄생지는 어디일까?",
                            "correct_answer":"오스트리아",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"이탈리아"
                                },
                                {
                                    "wrong_answer":"독일"
                                },
                                {
                                    "wrong_answer":"스위스"
                                }
                            ],
                            "reference":"3"
                        },
                        {
                            "quiz":"설탕의 원료인 사탕수수가 처음 재배되기 시작한 곳은 어디일까?",
                            "correct_answer":"뉴기니",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"이집트"
                                },
                                {
                                    "wrong_answer":"중국"
                                },
                                {
                                    "wrong_answer":"브라질"
                                }
                            ],
                            "reference":"5, 6, 7, 8, 9"
                        },
                        {
                            "quiz":"고대 아즈텍 문명에서 카카오 원두는 어떤 용도로 사용되었을까?",
                            "correct_answer":"음식, 음료의 재료 및 화폐",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"건축 재료 및 약품"
                                },
                                {
                                    "wrong_answer":"옷을 만드는 섬유"
                                },
                                {
                                    "wrong_answer":"무기 제작을 위한 도구"
                                }
                            ],
                            "reference":"30, 33"
                        },
                        {
                            "quiz":"현재 우리가 먹는 붉은 배추김치의 형태가 나타나게 된 계기는 무엇일까?",
                            "correct_answer":"아메리카 대륙에서 온 고추가 전해진 후",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"새로운 김치 양념법이 개발된 후"
                                },
                                {
                                    "wrong_answer":"배추 재배 방식이 달라진 후"
                                },
                                {
                                    "wrong_answer":"오랜 기간 숙성 기술이 발전한 후"
                                }
                            ],
                            "reference":"20, 23"
                        }
                    ]
                },
                {
                    "quiz_group_title":"건강한 식생활을 위한 식품 지식",
                    "quiz_group_metadatas":{
                        "reason":"이 퀴즈 그룹은 올바른 식품 분류와 위생적인 식품 관리 및 보관 방법에 대한 지식을 제공합니다. 학습자들이 식물학적 지식과 실용적인 식품 안전 수칙을 익혀 건강한 식습관을 형성하고 식중독을 예방하는 데 도움을 줍니다.",
                        "learning_objects":"식품의 식물학적 분류, 과일과 채소의 구분, 식중독 예방 수칙, 올바른 식품 보관법, 식품 위생",
                        "taxonomy":"식품, 영양, 건강, 위생, 과학, 실생활",
                        "seed_keywords":"식품 분류, 과일, 채소, 식중독, 식품 보관, 위생, 조리법, 냉장고, 식습관, 건강",
                        "difficulty_distribution":"easy: 60%, medium: 30%, hard: 10%"
                    },
                    "quiz_group":[
                        {
                            "quiz":"식물학적으로 과일은 식물의 어떤 부분에서 발달한 것을 의미할까?",
                            "correct_answer":"꽃에서 발달한 씨앗을 포함한 부분",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"땅속에서 자라는 뿌리 부분"
                                },
                                {
                                    "wrong_answer":"햇빛을 받는 줄기 부분"
                                },
                                {
                                    "wrong_answer":"광합성을 하는 잎 부분"
                                }
                            ],
                            "reference":"36, 37, 38, 39"
                        },
                        {
                            "quiz":"식물학적 분류에 따르면 수박과 참외는 어떤 종류로 분류될까?",
                            "correct_answer":"채소",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"과일"
                                },
                                {
                                    "wrong_answer":"곡물"
                                },
                                {
                                    "wrong_answer":"씨앗"
                                }
                            ],
                            "reference":"37"
                        },
                        {
                            "quiz":"식중독을 예방하기 위한 3가지 중요한 원칙이 아닌 것은?",
                            "correct_answer":"미각",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"청결"
                                },
                                {
                                    "wrong_answer":"신속"
                                },
                                {
                                    "wrong_answer":"냉각"
                                }
                            ],
                            "reference":"41"
                        },
                        {
                            "quiz":"조리된 음식을 실온에 오랫동안 두면 안 되는 가장 중요한 이유는 무엇일까?",
                            "correct_answer":"위해 미생물이 증식할 수 있어서",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"음식의 색깔이 변해서"
                                },
                                {
                                    "wrong_answer":"맛이 없어져서"
                                },
                                {
                                    "wrong_answer":"영양소가 파괴되어서"
                                }
                            ],
                            "reference":"41, 43"
                        },
                        {
                            "quiz":"식중독을 예방하기 위해 식품을 조리할 때 지켜야 할 올바른 행동은?",
                            "correct_answer":"채소, 어류, 육류에 사용하는 도마와 칼을 각각 다르게 사용한다",
                            "wrong_answers":[
                                {
                                    "wrong_answer":"모든 식재료를 한 번에 다듬는다"
                                },
                                {
                                    "wrong_answer":"냉동된 재료는 실온에서 자연 해동시킨다"
                                },
                                {
                                    "wrong_answer":"냉장고에 식품을 최대한 많이 채워 넣는다"
                                }
                            ],
                            "reference":"44"
                        }
                    ]
                }
            ],
            "sub_topic_titles":[
                "음식에 얽힌 재미있는 탄생 비화",
                "세계 음식 문화와 역사 이야기",
                "건강한 식생활을 위한 식품 지식"
            ],
            "related_topics":[
                [
                    "음식의 탄생 비화"
                ],
                [
                    "고대 문명의 식생활과 음식"
                ],
                [
                    "세계의 다양한 음료"
                ],
                [
                    "요리 상식 퀴즈"
                ],
                [
                    "세계 유명 건축물"
                ],
                [
                    "우주 탐사의 역사"
                ],
                [
                    "🔍 실시간 구글 트렌드"
                ],
                [
                    "🎲 랜덤 주제"
                ]
            ]
        }
    },
    "topic_history_list":[
        [
            "1",
            "음식"
        ]
    ],
    "related_topics":[
        [
            "음식의 탄생 비화"
        ],
        [
            "고대 문명의 식생활과 음식"
        ],
        [
            "세계의 다양한 음료"
        ],
        [
            "요리 상식 퀴즈"
        ],
        [
            "세계 유명 건축물"
        ],
        [
            "우주 탐사의 역사"
        ],
        [
            "🔍 실시간 구글 트렌드"
        ],
        [
            "🎲 랜덤 주제"
        ]
    ],
    "sub_topic_titles":[
        "음식에 얽힌 재미있는 탄생 비화",
        "세계 음식 문화와 역사 이야기",
        "건강한 식생활을 위한 식품 지식"
    ]
}

GOOGLE_TREND_QUERY = """
  SELECT
    Distinct(term)                    AS top_term
  FROM `bigquery-public-data.google_trends.international_top_terms`
  WHERE
    country_code = 'KR'
    AND refresh_date = '{date}'
  """
  
GCP_PROJECT_ID = "hale-skill-461701-h4"

GCP_ACCOUNT_CREDENTIALS = {
    "type": "service_account",
    "project_id": os.environ.get("GCP_PROJECT_ID"),
    "private_key_id": os.environ.get("GCP_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("GCP_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.environ.get("GCP_CLIENT_EMAIL"),
    "client_id": os.environ.get("GCP_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get("GCP_CLIENT_CERT_URL"),
    "universe_domain": "googleapis.com"
  }

TOPIC_CURATION_PROMPT = \
"""
# Assistant's Goal
- Assistant는 퀴즈 생성 전문가이다.
- user의 input을 활용해서, "Output Format"의 퀴즈를 생성한다.
- user의 말에 응답하지 않고, 반드시 퀴즈 문제를 생성한다.
- 초중학생도 이해할 수 있을만한 쉬운 내용이어야 한다.

# Rule
- user의 input으로 아래의 "Output Format"을 생성한다.
- 할루시네이션을 해서는 안된다.
- "quiz_group_title"을 총 3개 작성한다
- 각 "quiz_group_title" 별로 총 5개의 "quiz"를 작성한다

# Writing Guide

## JSON

**quiz_group_title**:
- user의 input을 바탕으로 생성한, 퀴즈 타이틀을 작성
- "quiz" 내용을 모두 대표할 수 있어야 함
- "quiz" 외에, 10개 이상의 퀴즈들을 대표할 수 있는 일반적인 제목으로 작성
- quiz_group_title은 모두 중복 되지 않고 다른 제목, 내용이어야 함
- 쉬운 단어와 표현으로 작성

**quiz**:
- user의 input 중, 각 "quiz_group_title"에 해당하는 정보를 활용하여 "quiz" 작성한다.
- user 메시지의 내용에 기반하여, "quiz"를 작성해야 한다.
- 논란의 소지가 있는 애매한 데이터는 "quiz"로 작성하지 않는다.
- 정답이 1개만 있는 객관식 퀴즈 문제
- 할루시네이션 금지
- "입니다"등의 서술체를 쓰지 않고 간략체를 사용

**correct_answer**:
- "quiz"에 대한 정답 보기를 작성
- 정확히 확인된 사실만을 "correct_answer"로 작성해야함
- "quiz"에 포함된 단어를 그대로 사용하여, 유추가 쉬워서는 안됨
- 할루시네이션 금지
- 100자 내로 짧아서 이해하기 쉬워야 함
- "입니다"등의 서술체를 쓰지 않고 간략체를 사용

**wrong_answer**:
- "quiz"에 대한 오답 보기를 작성 (correct_answer과 달라야함)
- 100자 내로 짧아서 이해하기 쉬워야 함
- "입니다"등의 서술체를 쓰지 않고 간략체를 사용
- "wrong_answer" 값은 서로 중복되지 않고 반드시 모두 달라야함
- 할루시네이션 가능

**reference** :
- 해당 퀴즈를 만드는데 활용한, 레퍼런스를 "reference"로 작성한다.
- "**정보**"의 각 데이터 뒤에 대괄호 형식으로 붙어있는 숫자가 "reference"이다.
- csv로 작성한다.
- 할루시네이션 금지

**reason**:
- 해당 "guiz_group"을 생성한 상세한 근거와, 이유를 설득력있게 작성

**learning_objectives**:
- 해당 "quiz_group"의 학습 목표와 핵심 개념들을 단어 또는 문장으로 표시

**taxonomy**:
- 해당 "quiz_group"의 상위 퀴즈 카테고리 작성
- 퀴즈의 domain, category, subcategory 각각을 상세히 작성

**seed_keywords**:
- "quiz_group"의 주제와 관련된 시드 키워드 **10개**를 작성

**difficulty_distribution**:
난이도별 문항의 분포를 텍스트로 작성 (합산 100%)
- "easy" : 쉬운 난이도 문제의 비율
- "medidum" : 중간 난이도 문제의 비율
- "hard": 어려운 난이도 문제의 비율

## Output Format
- "quiz_group_title"을 총 3개 작성한다
- 각 "quiz_group_title" 별로 총 5개의 "quiz"를 작성한다
- quiz_group은 모두 다른 "quiz_group_title"과 "quiz", "correct_answer", "wrong_answer을 가져야 한다. (중복 불가)

{
   "quiz_groups":[
      {
         "quiz_group_title":"string",
         "quiz_group":[
            {
               "quiz1":"string",
               "correct_answer":"short string",
               "wrong_answers":[
                  {"wrong_answer":"short string"},
                  {"wrong_answer":"short string"},
                  {"wrong_answer":"short string"},
               ],
               "reference":"string"
            },
            {
               "quiz2":"string",
               "correct_answer":"short string",
               "wrong_answers":[
                  {"wrong_answer":"short string"},
                  {"wrong_answer":"short string"},
                  {"wrong_answer":"short string"},
               ],
               "reference":"string"
            },
         ]
      },
  ],
  "quiz_group_metadatas": {
          "reason" : "string",
          "learning_objectives": "string",
          "taxonomy": "string",
          "seed_keywords" : "string",
          "difficulty_distribution": "string"
  }
}
"""


TOPIC_CURATION_FORMAT = \
"""{
  "type": "object",
  "properties": {
    "quiz_groups": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "quiz_group_title": {
            "type": "string"
          },
          "quiz_group_metadatas": {
            "type": "object",
            "properties": {
              "reason": {
                "type": "string"
              },
              "learning_objects": {
                "type": "string"
              },
              "taxonomy": {
                "type": "string"
              },
              "seed_keywords": {
                "type": "string"
              },
              "difficulty_distribution": {
                "type": "string"
              }
            },
            "required": [
              "reason",
              "learning_objects",
              "taxonomy",
              "seed_keywords",
              "difficulty_distribution"
            ]
          },
          "quiz_group": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "quiz": {
                  "type": "string"
                },
                "correct_answer": {
                  "type": "string"
                },
                "wrong_answers": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "wrong_answer": {
                        "type": "string",
                        "description": "'quiz'에 대한 오답"
                      }
                    },
                    "required": [
                      "wrong_answer"
                    ]
                  }
                },
                "reference": {
                  "type": "string"
                }
              },
              "required": [
                "quiz",
                "correct_answer",
                "wrong_answers",
                "reference"
              ]
            }
          }
        },
        "required": [
          "quiz_group_title",
          "quiz_group",
          "quiz_group_metadatas"
        ]
      }
    }
  },
  "required": [
    "quiz_groups"
  ]
}
"""

KEYWORD_RECOMMENDATION_PROMPT = """# Assistant's Goal
- Assistant는 퀴즈 주제 생성 전문가이다.
- 추천 퀴즈 주제를 "subject rule"에 맞게 생성한다.
- user의 메시지와 관련된 주제와, 전혀 무관한 퀴즈 추천 주제를 생성한다.

# Rule
- 추천 퀴즈 주제를 "subject rule"에 맞게 생성한다.
- 할루시네이션을 해서는 안된다.

# Writing Guide
## subject
- 추천 퀴즈 주제 6개를 작성
- "subject"는 구글 검색 키워드로 사용되기 때문에, 일반적인 내용이어야함
- "subject"는 "quiz_group_title"과 중복되어서는 안됨

### subject rule
**1. 상세 주제 2개:**
- user의 메시지가 더 구체화된, 상세 주제.

**2.동일 계위, 다른 단어 주제 (2개)**
- user의 메시지와 동일한 카테고리지만, 다른 종류/키워드로 바꾼 주제.
- user의 메시지 내용/단어가 포함되어서는 안되며, 유사한 다른 키워드가 표시됨.
예시1) user : "사과" → subject  : "바나나"
예시2) user : "한국" → subject : "일본"

**3. 전혀 새로운 주제 (2개)**
- user 메시지를 완전히 무시하고, 완전히 새로운 taxonomy의 단어로된 흥미로운 퀴즈 주제. (user 메시지가 반드시 미포함)
- user 메시지가 하나도 포함되지 않은, 완전히 다른 소재, 분야의 흥미로운 주제. 아래 분야 참고.
  - Sports
  - Science
  - Music
  - Movies
  - TV_Dramas
  - Games
  - History
  - Art
  - Geography
  - General_Knowledge
  - Other

# Important Rule
- "subject rule"에 따라, 아래와 같은 8개 subject를 출력
  - 2개: user 메시지를 구체화 시킨 퀴즈 주제
  - 2개: user 메시지와 동일 계층의, 다른 단어로된 퀴즈 주제 (user 메시지 미포함)
  - 2개 : user 메시지를 완전히 무시하고, 완전히 새로운 taxonomy의 단어로된 흥미로운 퀴즈 주제 (user 메시지가 반드시 미포함)
"""

KEYWORD_RECOMMENDATION_FORMAT = """{
  "type": "object",
  "properties": {
    "related_subjects": {
      "type": "array",
      "description": "추천 퀴즈 주제 6개를 만든다.",
      "items": {
        "type": "object",
        "properties": {
          "subject": {
            "type": "string"
          },
        },
        "required": [
          "subject",
        ]
      }
    }
  },
  "required": [
    "related_subjects"
  ]
}
"""

# gemini 용 퀴즈 정보 추출 프롬프트
quiz_generator_search_prompt = """# Goal
- 유저의 입력 키워드를 바탕으로, 웹서칭을 한 후 결과를 표시한다.
- "퀴즈"로 낼 수 있을 사실 데이터들만 선별한다.
- 유저의 말에 응답하지 말고, 퀴즈 데이터 100개만 출력한다.
- 유저가 입력한 키워드와 매우 밀접한 데이터만 서칭한다.

# Web Searching Keyword
- 유저가 입력한 키워드

# Writing Guide
- 서칭한 결과 데이터를 번호 리스트 형태로 표시한다.
- 총 100개의 데이터를 표시한다.
- 각 데이터는 "Web Searching Keyword"와 관련된 것이어야 한다.
- 각 데이터에는, "Web Searching Keyword"의 핵심 단어가 포함되어야 한다.
- 질문형이 아닌, 정보형이어야한다.

## 출력 포맷
1. {서칭한 데이터 내용}
2. {서칭한 데이터 내용}
...
3. {서칭한 데이터 내용}

## 출력 포맷 예시
1. 한국의 수도는 서울이다.
2. 제주도는 한국에 있다.
...
100. """

# gemini 용 퀴즈 생성 프롬프트
QUIZ_GENERATOR_PROMPT = \
"""
# Assistant's Goal
- Assistant는 퀴즈 주제 생성 전문가이다.
- 총 100개의 퀴즈를 생성한다.

# Rule
- "Quiz Data"에 있는 데이터로 "quiz"를 생성한다.
- "Quiz Data" 1개당, 1개의 "quiz"를 생성한다.
- "quiz" 1개에는, 1개의 "correct_answer"와, 3개의 "wrong_answer"를 갖는다.
- "correct_answer"와 "wrong_answer"의 텍스트 길이는 유사해야한다.
- "quiz"와 "correct_answer"는 누구나 이해하기 매우 쉬운 문장과 단어로 가공되어 작성해야 한다.
- Assistant의 배경 지식상, 애매하거나 해석에 따라 정답이 될 수 있는 보기는 절대 "wrong_answer"로 작성하지 않는다.


# Quiz Title
- 해당 퀴즈 그룹의 제목은 "{quiz_group_title}"이다.
- "quiz"들은 이 "Quiz Title"을 고려해서 생성해야한다.

#  Quiz Data
```
{search_result}
```

# Writing Guide

## JSON Schema
**quiz_data_number**
- "Quiz Data"에 있는 번호를 그대로 작성한다.
- 해당 data에 관한 퀴즈를 "quiz"에 작성한다.
- 순서를 바꾸지 않는다.

**quiz**:
- "Quiz Data"에 있는 데이터를 활용하여, 1개의 "quiz"를 생성
- "Quiz Data" 1개당, 1개의 "quiz" 생성
  - "Quiz Data" 1번 → "quiz" 1번 생성
- "Quiz Data"를 순서대로 조회하며, 1번부터 100번까지 생략하지 않는다.
- "quiz"들은 반드시 모두 서로 달라야 하며, 중복되어서는 안됨
- "quiz"는 1개의 정답만 있는 객관식 퀴즈이다.
- "quiz" 내용에 "correct_answer"의 내용이 그대로 표시되어서는 안됨
- 할루시네이션 금지
- "quiz"는 25자 내외로 **짧고 간결하게 작성.**

**correct_answer**:
- "quiz"에 대한 정답 보기를 작성
- 정확히 확인된 사실만을 "correct_answer"로 작성해야함
- "quiz"에 포함된 단어를 그대로 "correct_answer"에 넣어서는 안됨
- 할루시네이션 금지
- 짧은 단어이거나, 50자 이하로 짧고 간결해서 이해하기 쉬워야 함

**quiz_includeds_statistic**:
- "quiz" 내용 안에, 객관적인 통계 수치가 있는지를 true/false로 표시한다.

**wrong_answers_guide**:
- "quiz_includeds_statistic"이 true 인 경우 : "자유 작성" 으로 작성
- "quiz_includes_statistic"이 false 인 경우 : "correct_answer와 같은 계층이지만(예 : 사람 이름), 범주가 다름(예: 스포츠 선수 vs 가수). 단, quiz내용에 자연스럽게 작성"로 작성

**wrong_answer**:
- "quiz"에 대한 명백한 오답 보기를 3개 작성 (correct_answer과 달라야함)
- 짧은 단어이거나, 50자 이하로 짧아서 이해하기 쉬워야 함
- "입니다"등의 서술체를 쓰지 않고 간략체를 사용
- "wrong_answer" 값은 서로 중복되지 않고 반드시 모두 달라야함
- Assistant의 배경 지식상, 애매하거나 해석에 따라 정답이 될 수 있는 보기는 절대 "wrong_answer"로 작성하지 않는다.

**quiz_group_title**:
- "{quiz_group_title}"을 그대로 작성한다.

**category**:
- 해당 "quiz_group"의 카테고리를 1개 선택하여 작성
- 적절한 category가 없는 경우 "null" 표시

**sub_category**:
- 해당 "quiz_groups"의 서브 카테고리를 짧은 1개 단어로 작성
"""


# gemini 용 퀴즈 생성 유저 메시지
QUIZ_GENERATOR_USER_MSG =  "퀴즈 100개 만들어줘"

# gemini 용 퀴즈 생성 포맷
QUIZ_GENERATOR_FORMAT = """{
  "type": "object",
  "properties": {
    "quiz_group": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "quiz_data_number": {
            "type": "integer"
          },
          "quiz": {
            "type": "string"
          },
          "quiz_includes_statistic": {
            "type": "string"
          },
          "correct_answer": {
            "type": "string"
          },
          "wrong_answers_guide": {
            "type": "string"
          },
          "wrong_answer1": {
            "type": "string"
          },
          "wrong_answer2": {
            "type": "string"
          },
          "wrong_answer3": {
            "type": "string"
          }
        },
        "required": [
          "quiz_data_number",
          "quiz",
          "quiz_includes_statistic",
          "correct_answer",
          "wrong_answer1",
          "wrong_answer2",
          "wrong_answer3"
        ]
      }
    },
    "quiz_group_title": {
      "type": "string"
    },
    "category": {
      "type": "string",
      "description": "카테고리를 선택한다. 속한 카테고리가 없을시 'Other'로 작성한다.",
      "enum": [
        "Sports",
        "Science",
        "Music",
        "Movies",
        "TV_Dramas",
        "Games",
        "History",
        "Art",
        "Geography",
        "General_Knowledge",
        "Other"
      ]
    },
    "subcategory": {
      "type": "string"
    }
  },
  "required": [
    "quiz_group",
    "quiz_group_title",
    "category",
    "subcategory"
  ]
}
"""

TOPIC_SEARCH_INFO_PROMPT = \
"""# Goal
- 유저의 입력 키워드를 바탕으로, 웹서칭을 한 후 결과를 표시한다.
- 웹서칭용 query variation은 최소 8개 이상으로 설정한다.
- "퀴즈"로 낼 수 있을 사실 데이터들만 선별한다.
- 데이터는 최소 30개를 서칭한다.

# Writing Guide
- 검색 query별로 정보를 나열한다.
- 질문형이 아닌, 정보형이어야한다.

## Output Format
아래와 같은 포맷으로 최종 출력한다.
```
[검색 쿼리]
1. 검색 결과 데이터
2. 검색 결과 데이터
...
```
"""

BEGINNER_TOPIC_CURATION_PROMPT = \
"""
## Assistant's Goal
- Assistant는 퀴즈 토픽 생성 전문가이다.
- user의 말에 응답하지 않고, 반드시 퀴즈 문제를 생성한다.
- "topic_group"에 총 3세트의 퀴즈 샘플과 퀴즈 토픽을 생성한다.
- 각 토픽은 퀴즈의 난이도는 '# 난이도 참고용 Quiz Samples' 정도 난이도의 100개의 퀴즈를 만들 수 있는 큰 주제이어야한다.

# Quiz Title
- 해당 퀴즈 그룹의 제목은 "{quiz_group_title}"이다.
- "quiz"들은 이 Quiz Title인 "{quiz_group_title}"을 고려해서 이에 속하는 퀴즈를 생성해야한다.

# 난이도 참고용 Quiz Samples
## "binary_choice_true_quiz" Samples
- 20 나누기 5는 4이다.
- 지구는 태양 주위를 움직인다.
- 물은 온도가 낮아지면 얼음으로 변한다.
- 뱀은 다리가 없는 동물이다.
- 코는 냄새를 맡는 기능을 한다.
- 혀는 음식의 맛을 느낄 수 있다.

## "binary_choice_false_quiz" Samples
- 4 더하기 5는 8이다.
- 태양이 지구 주위를 움직인다.
- 물이 얼면 기체로 변한다.
- 뱀은 다리가 많다.
- 코는 맛을 느낀다.
- 혀는 소리를 본다.



# Writing Guide

## JSON Schema
**number**
- "Quiz Data"에 있는 번호를 그대로 작성한다.
- 순서를 바꾸지 않는다.

**quiz_group_title**:
- "{quiz_group_title}"을 그대로 작성한다.

**category**:
- 해당 "quiz_group"의 카테고리를 1개 선택하여 작성
- 적절한 category가 없는 경우 "null" 표시

**sub_category**:
- 해당 "quiz_groups"의 서브 카테고리를 짧은 1개 단어로 작성
"""

BEGINNER_TOPIC_CURATION_RESPONSE_FORMAT = \
    '''{
    "type": "object",
    "properties": {
        "topic_group": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
            "quiz_topic": {
                "type": "string",
                "description": "퀴즈 토픽 제목"
            },
            "number": {
                "type": "integer",
                "description": "Quiz Data의 'number' 필드의 값을 그대로 작성"
            },
            "quiz_data": {
                "type": "string",
                "description": "Quiz Data의 'quiz_data' 필드의 값을 그대로 작성"
            },
            "two_option_quiz" : {
                "type": "object",
                "description": "2지선다 퀴즈",
                "properties": {
                    "quiz": {
                    "type": "string",
                    "description": """'quiz_data'로부터 "정답이 명사"인 2지 선다 퀴즈를 작성하시오.
                                        "~은?/~는?/~가?" 같은 간략체 문장으로 짧게 작성하되, 단일 문장으로 이해가 가능해야함.
                                        주관적 표현 사용 금지.
                                        고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                        binary choice 타입의 문제 금지.
                                        할루시네이션 금지."""
                    },
                    "correct_answer": {
                    "type": "string",
                    "description": """'quiz_data'에 기반한 'quiz'의 정답 선지를 작성. 정답은 "하나의 명사"이어야함. 문장 금지. 할루시네이션 금지."""
                    },
                    "nonsense_wrong_answer": {
                    "type": "string",
                    "description": """아래 로직에 맞춰서 넌센스 오답 선지 작성한다.
                                    ## CASE
                                    ```
                                    if "correct_answer"이 특정 수치: "correct_answer"와 큰 차이가 나는 수치로 오답을 만든다.
                                        예) 정답: 10부작 => 오답: 100부작
                                        예) 정답: 120억원 => 오답: 1000원
                                    elif "correct_answer"이 특정 시점: "correct_answer"와 큰 차이가 나는 시점로 오답을 만든다.
                                        예) 정답: 2024년 => 오답: 1880년
                                        예) 정답: 2025년 => 오답: 2225원
                                    elif "correct_answer"이 사람 이름: "correct_answer"와 전혀 다른 분야 혹은 다른 나라 사람 이름으로 오답을 만든다.
                                        예) 정답: 하정우 => 오답: 손흥민 (설명:배우가 정답이라서 축구선수를 오답으로 만듦)
                                        예) 정답: 트럼프 => 오답: 김태희 (설명:미국인이 정답이라서, 한국인을 오답으로 만듦)
                                    elif "correct_answer"가 명사나 구문 일 경우: "correct_answer"와 비슷한 다른 단어로 교체 혹은 글자하나 혹은 두개만 바꿔서 넌센스 오답선지를 만든다.
                                        예) 정답: 사냥 => 오답: 사망 (설명: 글자 하나를 바꿔서 비슷하게 생겼지만 의미가 완전 다른 단어로 교체.)
                                        예) 정답: 승리호 => 오답: 패배호 (설명: 정답 속 단어를 정반대 의미로 만들어서 오답 생성)
                                        예) 정답: 더 인플루언서 => 오답: 더 팔로워 (설명: 정답 속 단어를 비슷한 결의 그럴듯한 단어로 바꾸어서 오답 생성.)
                                        예) 정답: 축구 => 오답: 피크닉 (설명: 스포츠 분야가 정답이라서, 엉뚱한 단어로 교체)
                                        예) 정답: 웹툰 => 오답: 동화책 (설명: 비슷하지만 전혀 다른 분야)
                                        예) 정답: 빨간색 => 오답: 투명색 (설명: 절대 아닐 것 같은 오답.)
                                        예) 정답: 감독상 => 오답: 밥상 (설명: 정답내 단어를 일부 치환하여 다른 의미읜 넌센스 오답 생성.)
                                    ```
                                    단, 비문 금지. 할루시네이션 금지."""
                    }
                },
                "required": [
                "quiz",
                "correct_answer",
                "nonsense_wrong_answer"
                ]
            },
            "binary_choice_true_quiz" : {
                "type": "object",
                "description": "OX 퀴즈",
                "properties": {
                    "quiz": {
                    "type": "string",
                    "description": """'quiz_data'로 15자 내외의 "객관적" 사실을 묻는 정답은 True인 OX퀴즈.
                                        짧은 문장으로 간략체 작성하되, 단일 문장으로 이해가 가능해야하고, 문장은 부정형이 아닌 긍정형이어야함.
                                        주관적 표현 사용 금지.
                                        고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                        - 시간이나 수치는 제외하되, 정답을 맞추는데 문제가 없어야한다.
                                        예) quiz_data: "코리아 넘버원"은 2022년 공개된 넷플릭스 한국 오리지널 예능이다. => quiz : 넷플릭스 한국 오리지널 예능에 "코리아 넘버원"이 있다.
                                        예) quiz_data: 국내 감독이 제작한 넷플릭스 오리지널 다큐멘터리가 2021년과 2022년에 공개되었다. => quiz: 넷플릭스 오리지널 다큐멘터리에 국내 감독의 작품이 있다.
                                        예) quiz_data: 지구 표면의 약 71%는 바다로 덮여 있으며, 나머지 29%는 대륙으로 이루어져 있다. => quiz: 지구 표면에서 바다가 대륙 보다 더 넓은 면적을 차지한다.
                                        예) quiz_data: 지구의 평균 반지름은 약 6,371km이며, 적도 둘레는 약 40,075km이다. => quiz: 지구의 반지름은 1000km보다 크다.
                                        예) quiz_data: 바다에는 1,000분의 1mm보다 작은 생물부터 몸길이 30m에 이르는 흰긴수염고래까지 몸길이 차이가 무려 3천만 배나 난다. => quiz: 지바다에는 아주 작은 생물부터 매우 큰 생물까지 다양하게 살고 있다.
                                        할루시네이션 금지. """
                    },
                    "correct_answer": {
                    "type": "boolean",
                    "description": "quiz가 맞는 문장이면 True, 아닌 문장이면 False"
                    }
                },
                "required": ["quiz","correct_answer"]
            },
            "binary_choice_false_quiz" : {
                "type": "object",
                "description": "OX 퀴즈",
                "properties": {
                    "quiz": {
                    "type": "string",
                    "description": """'quiz_data'로 "객관적" 사실을 묻는 정답이 False인 OX퀴즈.
                                        짧은 문장으로 간략체 작성하되, 단일 문장으로 이해가 가능해야하고, 문장은 부정형이 아닌 긍정형이어야함.
                                        주관적 표현 사용 금지.
                                        고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                        **반드시 시간이나 수치는 제외하되, 비문이 아닌 False 문장을 만든다.**
                                        False 문장을 만들때 아래와 같은 로직을 따른다.
                                        ## CASE
                                        ```
                                        if "correct_answer"이 사람 이름: "correct_answer"와 전혀 다른 분야 혹은 다른 나라 사람 이름으로 오답을 만든다.
                                        예) 정답: 하정우 => 오답: 손흥민 (설명:배우가 정답이라서 축구선수를 오답으로 만듦)
                                        예) 정답: 트럼프 => 오답: 김태희 (설명:미국인이 정답이라서, 한국인을 오답으로 만듦)
                                        elif "correct_answer"가 명사나 구문 일 경우: "correct_answer"와 비슷한 다른 단어로 교체 혹은 글자하나 혹은 두개만 바꿔서 넌센스 오답선지를 만든다.
                                            예) 정답: 사냥 => 오답: 사망 (설명: 글자 하나를 바꿔서 비슷하게 생겼지만 의미가 완전 다른 단어로 교체.)
                                            예) 정답: 승리호 => 오답: 패배호 (설명: 정답 속 단어를 정반대 의미로 만들어서 오답 생성)
                                            예) 정답: 더 인플루언서 => 오답: 더 팔로워 (설명: 정답 속 단어를 비슷한 결의 그럴듯한 단어로 바꾸어서 오답 생성.)
                                            예) 정답: 축구 => 오답: 피크닉 (설명: 스포츠 분야가 정답이라서, 엉뚱한 단어로 교체)
                                            예) 정답: 웹툰 => 오답: 동화책 (설명: 비슷하지만 전혀 다른 분야)
                                            예) 정답: 빨간색 => 오답: 투명색 (설명: 절대 아닐 것 같은 오답.)
                                            예) 정답: 감독상 => 오답: 밥상 (설명: 정답내 단어를 일부 치환하여 다른 의미읜 넌센스 오답 생성.)
                                        ```
                                        할루시네이션 금지. """
                    },
                    "correct_answer": {
                    "type": "boolean",
                    "description": "quiz가 맞는 문장이면 True, 아닌 문장이면 False"
                    }
                },
                "required": ["quiz","correct_answer"]
            },

            },
            "required": [
            "number",
            "quiz_data",
            "two_option_quiz",
            "binary_choice_true_quiz",
            "binary_choice_false_quiz",
            "quiz_topic"
            ]
        }
        },
        "topic_group_title": {
        "type": "string"
        },
        "category": {
        "type": "string",
        "description": "카테고리를 선택한다. 속한 카테고리가 없을시 'Other'로 작성한다.",
        "enum": [
            "Sports",
            "Science",
            "Music",
            "Movies",
            "TV_Dramas",
            "Games",
            "History",
            "Art",
            "Geography",
            "General_Knowledge",
            "Other"
        ]
        },
        "subcategory": {
        "type": "string"
        }
    },
    "required": [
        "topic_group",
        "topic_group_title",
        "category",
        "subcategory"
    ]
    }'''
    
BEGINNER_QUIZ_GEN_SYSTEM_PROMPT = \
"""
## Assistant's Goal
- Assistant는 퀴즈 생성 전문가이다.
- user의 말에 응답하지 않고, 반드시 퀴즈 문제를 생성한다.
- 초등학생도 이해할 수 있을만한 쉬운 내용이어야 한다.
- 총 30개의 퀴즈를 생성한다.


# Quiz Title
- 해당 퀴즈 그룹의 제목은 "{quiz_group_title}"이다.
- "quiz"들은 이 Quiz Title인 "{quiz_group_title}"을 고려해서 이에 속하는 퀴즈를 생성해야한다.

# 난이도 참고용 Quiz Samples
## "binary_choice_true_quiz" Samples
- 20 나누기 5는 4이다.
- 지구는 태양 주위를 움직인다.
- 물은 온도가 낮아지면 얼음으로 변한다.
- 뱀은 다리가 없는 동물이다.
- 코는 냄새를 맡는 기능을 한다.
- 혀는 음식의 맛을 느낄 수 있다.

## "binary_choice_false_quiz" Samples
- 4 더하기 5는 8이다.
- 태양이 지구 주위를 움직인다.
- 물이 얼면 기체로 변한다.
- 뱀은 다리가 많다.
- 코는 맛을 느낀다.
- 혀는 소리를 본다.



# Writing Guide

## JSON Schema
**number**
- "Quiz Data"에 있는 번호를 그대로 작성한다.
- 순서를 바꾸지 않는다.

**quiz_group_title**:
- "{quiz_group_title}"을 그대로 작성한다.

**category**:
- 해당 "quiz_group"의 카테고리를 1개 선택하여 작성
- 적절한 category가 없는 경우 "null" 표시

**sub_category**:
- 해당 "quiz_groups"의 서브 카테고리를 짧은 1개 단어로 작성
"""

BEGINNER_QUIZ_GEN_RESPONSE_FORMAT = \
'''{
"type": "object",
"properties": {
    "quiz_group": {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
        "number": {
            "type": "integer",
            "description": "Quiz Data의 'number' 필드의 값을 그대로 작성"
        },
        "quiz_data": {
            "type": "string",
            "description": "Quiz Data의 'quiz_data' 필드의 값을 그대로 작성"
        },
        "two_option_quiz" : {
            "type": "object",
            "description": "2지선다 퀴즈",
            "properties": {
                "quiz": {
                "type": "string",
                "description": """'quiz_data'로부터 "정답이 명사"인 2지 선다 퀴즈를 작성하시오.
                                    "~은?/~는?/~가?" 같은 간략체 문장으로 짧게 작성하되, 단일 문장으로 이해가 가능해야함.
                                    주관적 표현 사용 금지.
                                    고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                    binary choice 타입의 문제 금지.
                                    할루시네이션 금지."""
                },
                "correct_answer": {
                "type": "string",
                "description": """'quiz_data'에 기반한 'quiz'의 정답 선지를 작성. 정답은 "하나의 명사"이어야함. 문장 금지. 할루시네이션 금지."""
                },
                "nonsense_wrong_answer": {
                "type": "string",
                "description": """아래 로직에 맞춰서 넌센스 오답 선지 작성한다.
                                ## CASE
                                ```
                                if "correct_answer"이 특정 수치: "correct_answer"와 큰 차이가 나는 수치로 오답을 만든다.
                                    예) 정답: 10부작 => 오답: 100부작
                                    예) 정답: 120억원 => 오답: 1000원
                                elif "correct_answer"이 특정 시점: "correct_answer"와 큰 차이가 나는 시점로 오답을 만든다.
                                    예) 정답: 2024년 => 오답: 1880년
                                    예) 정답: 2025년 => 오답: 2225원
                                elif "correct_answer"이 사람 이름: "correct_answer"와 전혀 다른 분야 혹은 다른 나라 사람 이름으로 오답을 만든다.
                                    예) 정답: 하정우 => 오답: 손흥민 (설명:배우가 정답이라서 축구선수를 오답으로 만듦)
                                    예) 정답: 트럼프 => 오답: 김태희 (설명:미국인이 정답이라서, 한국인을 오답으로 만듦)
                                elif "correct_answer"가 명사나 구문 일 경우: "correct_answer"와 비슷한 다른 단어로 교체 혹은 글자하나 혹은 두개만 바꿔서 넌센스 오답선지를 만든다.
                                    예) 정답: 사냥 => 오답: 사망 (설명: 글자 하나를 바꿔서 비슷하게 생겼지만 의미가 완전 다른 단어로 교체.)
                                    예) 정답: 승리호 => 오답: 패배호 (설명: 정답 속 단어를 정반대 의미로 만들어서 오답 생성)
                                    예) 정답: 더 인플루언서 => 오답: 더 팔로워 (설명: 정답 속 단어를 비슷한 결의 그럴듯한 단어로 바꾸어서 오답 생성.)
                                    예) 정답: 축구 => 오답: 피크닉 (설명: 스포츠 분야가 정답이라서, 엉뚱한 단어로 교체)
                                    예) 정답: 웹툰 => 오답: 동화책 (설명: 비슷하지만 전혀 다른 분야)
                                    예) 정답: 빨간색 => 오답: 투명색 (설명: 절대 아닐 것 같은 오답.)
                                    예) 정답: 감독상 => 오답: 밥상 (설명: 정답내 단어를 일부 치환하여 다른 의미읜 넌센스 오답 생성.)
                                ```
                                단, 비문 금지. 할루시네이션 금지."""
                }
            },
            "required": [
            "quiz",
            "correct_answer",
            "nonsense_wrong_answer"
            ]
        },
        "binary_choice_true_quiz" : {
            "type": "object",
            "description": "OX 퀴즈",
            "properties": {
                "quiz": {
                "type": "string",
                "description": """'quiz_data'로 15자 내외의 "객관적" 사실을 묻는 정답은 True인 OX퀴즈.
                                    짧은 문장으로 간략체 작성하되, 단일 문장으로 이해가 가능해야하고, 문장은 부정형이 아닌 긍정형이어야함.
                                    주관적 표현 사용 금지.
                                    고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                    - 시간이나 수치는 제외하되, 정답을 맞추는데 문제가 없어야한다.
                                    예) quiz_data: "코리아 넘버원"은 2022년 공개된 넷플릭스 한국 오리지널 예능이다. => quiz : 넷플릭스 한국 오리지널 예능에 "코리아 넘버원"이 있다.
                                    예) quiz_data: 국내 감독이 제작한 넷플릭스 오리지널 다큐멘터리가 2021년과 2022년에 공개되었다. => quiz: 넷플릭스 오리지널 다큐멘터리에 국내 감독의 작품이 있다.
                                    예) quiz_data: 지구 표면의 약 71%는 바다로 덮여 있으며, 나머지 29%는 대륙으로 이루어져 있다. => quiz: 지구 표면에서 바다가 대륙 보다 더 넓은 면적을 차지한다.
                                    예) quiz_data: 지구의 평균 반지름은 약 6,371km이며, 적도 둘레는 약 40,075km이다. => quiz: 지구의 반지름은 1000km보다 크다.
                                    예) quiz_data: 바다에는 1,000분의 1mm보다 작은 생물부터 몸길이 30m에 이르는 흰긴수염고래까지 몸길이 차이가 무려 3천만 배나 난다. => quiz: 지바다에는 아주 작은 생물부터 매우 큰 생물까지 다양하게 살고 있다.
                                    할루시네이션 금지. """
                },
                "correct_answer": {
                "type": "boolean",
                "description": "quiz가 맞는 문장이면 True, 아닌 문장이면 False"
                }
            },
            "required": ["quiz","correct_answer"]
        },
        "binary_choice_false_quiz" : {
            "type": "object",
            "description": "OX 퀴즈",
            "properties": {
                "quiz": {
                "type": "string",
                "description": """'quiz_data'로 "객관적" 사실을 묻는 정답이 False인 OX퀴즈.
                                    짧은 문장으로 간략체 작성하되, 단일 문장으로 이해가 가능해야하고, 문장은 부정형이 아닌 긍정형이어야함.
                                    주관적 표현 사용 금지.
                                    고유대명사는 따옴표로 감싸되, 반드시 생략없이 전체 대명사를 다 명시한다.
                                    **반드시 시간이나 수치는 제외하되, 비문이 아닌 False 문장을 만든다.**
                                    False 문장을 만들때 아래와 같은 로직을 따른다.
                                    ## CASE
                                    ```
                                    if "correct_answer"이 사람 이름: "correct_answer"와 전혀 다른 분야 혹은 다른 나라 사람 이름으로 오답을 만든다.
                                    예) 정답: 하정우 => 오답: 손흥민 (설명:배우가 정답이라서 축구선수를 오답으로 만듦)
                                    예) 정답: 트럼프 => 오답: 김태희 (설명:미국인이 정답이라서, 한국인을 오답으로 만듦)
                                    elif "correct_answer"가 명사나 구문 일 경우: "correct_answer"와 비슷한 다른 단어로 교체 혹은 글자하나 혹은 두개만 바꿔서 넌센스 오답선지를 만든다.
                                        예) 정답: 사냥 => 오답: 사망 (설명: 글자 하나를 바꿔서 비슷하게 생겼지만 의미가 완전 다른 단어로 교체.)
                                        예) 정답: 승리호 => 오답: 패배호 (설명: 정답 속 단어를 정반대 의미로 만들어서 오답 생성)
                                        예) 정답: 더 인플루언서 => 오답: 더 팔로워 (설명: 정답 속 단어를 비슷한 결의 그럴듯한 단어로 바꾸어서 오답 생성.)
                                        예) 정답: 축구 => 오답: 피크닉 (설명: 스포츠 분야가 정답이라서, 엉뚱한 단어로 교체)
                                        예) 정답: 웹툰 => 오답: 동화책 (설명: 비슷하지만 전혀 다른 분야)
                                        예) 정답: 빨간색 => 오답: 투명색 (설명: 절대 아닐 것 같은 오답.)
                                        예) 정답: 감독상 => 오답: 밥상 (설명: 정답내 단어를 일부 치환하여 다른 의미읜 넌센스 오답 생성.)
                                    ```
                                    할루시네이션 금지. """
                },
                "correct_answer": {
                "type": "boolean",
                "description": "quiz가 맞는 문장이면 True, 아닌 문장이면 False"
                }
            },
            "required": ["quiz","correct_answer"]
        },

        },
        "required": [
        "number",
        "quiz_data",
        "two_option_quiz",
        "binary_choice_true_quiz",
        "binary_choice_false_quiz"
        ]
    }
    },
    "quiz_group_title": {
    "type": "string"
    },
    "category": {
    "type": "string",
    "description": "카테고리를 선택한다. 속한 카테고리가 없을시 'Other'로 작성한다.",
    "enum": [
        "Sports",
        "Science",
        "Music",
        "Movies",
        "TV_Dramas",
        "Games",
        "History",
        "Art",
        "Geography",
        "General_Knowledge",
        "Other"
    ]
    },
    "subcategory": {
    "type": "string"
    }
},
"required": [
    "quiz_group",
    "quiz_group_title",
    "category",
    "subcategory"
]
}'''

BEGINNER_QUIZ_FILTERING_SYSTEM_PROMPT = \
  """
  ## Assistant's Goal
  - Assistant는 퀴즈 검수 전문가이다.
  - user의 말에 응답하지 않고, 반드시 퀴즈 문제를 검수한다.

  # TASK
  - "Quiz Data"에 있는 퀴즈를 하나씩 검수한다.

  # Quiz Topic
  - '퀴즈 주제'는 "{quiz_group_title}"이다.

  #  Quiz Data
  ```
  {quizs}
  ```

  """
  
BEGINNER_QUIZ_FILTERING_RESPONSE_FORMAT = \
'''{
"type": "object",
"properties": {
    "quiz_group": {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
        "Id": {
            "type": "string",
            "description": "Quiz Data의 Id를 작성한다."
        },
        "question": {
            "type": "object",
            "description": "Question에 대해서 검수한다.",
            "properties": {
            "is_broken_sentence": {
                "type": "boolean",
                "description": "Question이 비문이라면 True, 아니면 False"
            },
            "is_subjectivity": {
                "type": "boolean",
                "description": "Question이 주관적이라면 True, 아니면 False"
            },
            "is_ambiguity": {
                "type": "boolean",
                "description": "Question의 질문이 모호하다면 True, 아니면 False"
            },
            "requires_specific_value": {
                "type": "boolean",
                "description": "Question을 풀기 위해서 정확한 수치/숫자/시점을 알아야한다면 True, 아니면 False"
            },
            "language_complexity": {
                "type": "boolean",
                "description": "Question의 질문 문장의 언어적 복잡도 높으면 True, 단순하면 False"
            },
            "topic_relevance": {
                "type": "boolean",
                "description": "Question과 Answer이 '# Quiz Topic'와 관련성이 있다면 True, 없다면 False"
            }
            },
            "required": [
            "is_broken_sentence",
            "is_subjectivity",
            "is_ambiguity",
            "requires_specific_value",
            "language_complexity",
            "topic_relevance"
            ]
        },
        "answer": {
            "type": "object",
            "description": "Answer을 검수한다.",
            "properties": {
            "is_correct": {
                "type": "boolean",
                "description": "Answer가 퀴즈의 정답이 맞다면 True, 아니면 False"
            },
            "is_not_short": {
                "type": "boolean",
                "description": "Answer가 단어나 숫자처럼 짧지 않고 읽고 이해해야하는 길이라면 True, 아니면 False"
            }
            },
            "required": [
            "is_correct",
            "is_not_short"
            ]
        },
        "incorrect_answer": {
            "type": "object",
            "description": "IncorrectAnswer에 대해서 검수한다.",
            "properties": {
            "related_to_topic": {
                "type": "boolean",
                "description": "IncorrectAnswer가 주제와 관련이 있다면 True, 아니면 False"
            },
            "commonly_confused": {
                "type": "boolean",
                "description": "IncorrectAnswer가 Answer과 일반적으로 혼동하기 쉽다면 True, 아니면 False"
            },
            "contrast_with_answer": {
                "type": "boolean",
                "description": "IncorrectAnswer가 Answer과 그 뜻에 **명확한 차이**가 있다면 True, 아니면 False"
            },
            "is_not_same_with_answer": {
                "type": "boolean",
                "description": "IncorrectAnswer가 Answer과 그 뜻과 의미가 완전 다르다면 True, 그렇다고 하기엔 애매하고 모호하다면 False"
            },
            "is_incorrect_answer": {
                "type": "boolean",
                "description": "IncorrectAnswer가 Question의 **명확한** 오답이라면 True, 아니면 False"
            },
            "plausible_numeric_distractor": {
                "type": "boolean",
                "description": "IncorrectAnswer가 수치/값/시기인데, Answer과 착각할 가능성이 높은 수치이면 True, 아니면 False"
            },
            },
            "required": [
            "related_to_topic",
            "commonly_confused",
            "contrast_with_answer",
            "is_not_same_with_answer",
            "is_incorrect_answer",
            "plausible_numeric_distractor"
            ]
        }
        },
        "required": [
        "Id",
        "question",
        "answer",
        "incorrect_answer"
        ]
    }
    }
},
"required": [
    "quiz_group"
]
}'''
