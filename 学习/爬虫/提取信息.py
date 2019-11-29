import requests
from bs4 import BeautifulSoup
try:
    url = "https://www.baidu.com"
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,'html.parser')
    a = soup.find_all(['div','a'])
    for t in a:
        print(t)
except:
    print("爬取失败")
