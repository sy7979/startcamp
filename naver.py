import requests
from bs4 import BeautifulSoup

response = requests.get("https://naver.com").text
soup = BeautifulSoup (response, "html.parser")

naver = soup.select(".ah_k")

for item in naver:
    print(item.text)