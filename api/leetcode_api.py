import json
import requests

# community thanks to https://github.com/bharathkalyans for his api
base_url = r"https://long-blue-tuna-coat.cyclic.app/"
leetcode_todays_question = r"/leetcode/todays-question"

# leetcode
CALLABLE_API = "https://leetcode.com/api/problems/algorithms/"


def get_daily_problem_as_dict():
    params = {
        "method": "GET"
    }
    response = requests.get(base_url + leetcode_todays_question, params=params).content
    return json.loads(response.decode("utf-8").replace("'", '"'))


def random_leetcode_problem():
    req = requests.get(url=CALLABLE_API)
    data = req.json()
    question_stats = data["stat_status_pairs"]
    question_stat = [q["stat"] for q in question_stats]
    question_stat = [question for question in question_stat if question is not None]
    questions = [[question["frontend_question_id"],
                  question["question__article__slug"]] for question in question_stat]
    return question_stats
