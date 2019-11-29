import requests
from bs4 import BeautifulSoup
try:
    url = "https://www.baidu.com"
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    print(soup.prettify())
except:
    print("爬取失败")
