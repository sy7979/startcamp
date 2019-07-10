# f = open('student.txt', 'w')
# f.write("안녕하세요")
# f.close()

import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

tr =  soup.select('tbody > tr')
with open("ssafy.txt", 'w') as f:
    for rate in tr:
        print(rate.select_one('.tit').text.strip())
        print(rate.select_one('.sale').text)
        f.write(rate.select_one('.tit').text.strip())
        f.write(rate.select_one('.sale').text)

# with open("ssafy2.txt", 'w') as f:
#     f.write(rate)
