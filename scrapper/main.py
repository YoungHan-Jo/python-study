import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://kr.indeed.com/jobs?q=java&l=%EC%84%9C%EC%9A%B8&radius=100&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div",{"class":"pagination"})

pages = pagination.find_all('a')
spans = []

for page in pages:
    spans.append(page.find("span"))

spans = spans[:-1]

print(spans)