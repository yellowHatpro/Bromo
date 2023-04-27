import requests
from bs4 import BeautifulSoup
import datetime


def get_daily_problem():
    # Get today's date in YYYY-MM-DD format
    today = datetime.date.today().strftime('%Y-%m-%d')

    # Send a GET request to the LeetCode Daily Challenge page for today's date
    url = 'https://leetcode.com/problemset/all'
    response = requests.get(url)
    # Parse the HTML content of the response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # Find the div element containing today's problem by searching for a link that ends with today's date
    daily_link = soup.find('a', {'href': f'/problems/daily-challenge/'})
    print(daily_link)
    # If no link is found, return an error message
    if not daily_link:
        return "No daily challenge found for today."

    # Follow the link to the daily challenge page
    response = requests.get(url + daily_link['href'])
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element containing today's problem
    daily_problem_div = soup.find('div', {'class': 'css-v3d350'})
    print(type(daily_problem_div.get_text().strip()))
    # Get the text content of the div and return it
    return daily_problem_div.get_text().strip()


CALLABLE_API = "https://leetcode.com/api/problems/algorithms/"

req = requests.get(url=CALLABLE_API)

data = req.json()

question_stats = data["stat_status_pairs"]
question_stat = [q["stat"] for q in question_stats]
question_stat = [question for question in question_stat if question is not None]
questions = [[question["frontend_question_id"],
              question["question__article__slug"]] for question in question_stat]
