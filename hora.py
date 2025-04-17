import requests
from bs4 import BeautifulSoup

url = "https://www.myhora.com/%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%97%E0%B8%B4%E0%B8%99/%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%97%E0%B8%B4%E0%B8%99-100%E0%B8%9B%E0%B8%B5-%E0%B8%9E.%E0%B8%A8.2479.aspx"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
hora = soup.find('div', class_="clm-1").find_all('div')

for i in hora:
    rank = i.find('div', class_="clm")
    print(rank)
