import requests
from bs4 import BeautifulSoup


url = "https://stackoverflow.com/questions"
res = requests.get(url, verify=False)
text = res.text

soup = BeautifulSoup(text, "html.parser")
questions = soup.select(".s-post-summary")
pagination = soup.select(".s-pagination")
# print(questions[0]["data-post-id"])
# print(pagination[0])

for pag in pagination:
    print("************")
    print(pag)
    # print(pag.get_text())
    # page = pag.select_one(".s-pagination--item").get_text()
    # print(page)

for question in questions:
    title = question.select_one(".s-link").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    # vote_count = question.select_one(
    #     ".s-post-summary--stats-item-number").get_text()
    # print(title, vote_count)
    # print(f"{user} - Titulo: \n{title.strip()}")
