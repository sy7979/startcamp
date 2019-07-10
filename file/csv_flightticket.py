import csv
import requests
from bs4 import BeautifulSoup

# 에러도 안뜨고 실행도 안되고!!

url = "https://flyairseoul.com/I/KO/viewAvail.do"
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

tr =  soup.select('tbody > td')
with open("airseoul.csv", 'w', encoding='utf-8', newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr:
        print(r.select_one('.tb1-start-time').text.strip())
        print(r.select_one('.point-color02').text.strip())
        print(r.select_one('.bookint-airlineticket-minimum-date').text)
        
        row = [r.select_one('.tb1-start-time').text.strip(),r.select_one('.bookint-airlineticket-minimum-date').text, r.select_one('.point-color02').text]
        csv_writer.writerow(row)