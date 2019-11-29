import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLtext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivlist(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find_all('tr','alt'):
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivlist(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校","省份",chr(12288)))#中文输出对齐的方法
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))


def main():
    ulist = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTMLtext(url)
    fillUnivlist(ulist,html)
    printUnivlist(ulist,20)

main()
