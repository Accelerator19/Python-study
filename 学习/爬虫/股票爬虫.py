import requests
import re
from bs4 import BeautifulSoup

def get_html_text(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parse_page(stock_list,html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())

def get_info_list(info_list,url,fpath):
    return ""

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    output = 'D://BaiduStockInfo.txt'
    stock_list = []
    html = get_html_text(stock_list_url)
    parse_page(stock_list,html)

main()
