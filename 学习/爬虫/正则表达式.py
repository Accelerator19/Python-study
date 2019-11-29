import requests
import re
from bs4 import BeautifulSoup
try:
    url = "https://beijing.youbianku.com/"
    r = requests.get(url,headers={'user-agent':'Mediapartners-Google'})
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')
    for a in soup.find_all('a'):
        if re.search(r'[1-9]\d{5}',str(a.string)):
            print(a)
except:
    print("爬取失败")
# match = re.search(r'[1-9]\d{6}','Bit 1008611 4567896')
# print(match.group(0))
