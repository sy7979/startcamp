import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section").text
soup = BeautifulSoup (res, 'html.parser')
rate = soup.select('body > div > table > tbody > tr:nth-child(1) > td.sale')

print(rate)