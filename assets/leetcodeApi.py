import requests

CALLABLE_API = "https://leetcode.com/api/problems/algorithms/"

req = requests.get(url=CALLABLE_API)

data = req.json()

question_stats = data["stat_status_pairs"]
question_stat = [q["stat"] for q in question_stats]
question_stat = [question for question in question_stat if question is not None]
questions = [[question["frontend_question_id"],
              question["question__article__slug"]] for question in question_stat]

