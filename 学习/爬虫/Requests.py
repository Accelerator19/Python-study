import requests
def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "Wrong"

if __name__=="__main__":
    url = "https://www.baidu.com"
    print(get_html(url))
