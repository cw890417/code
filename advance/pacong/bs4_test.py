import requests
from bs4 import BeautifulSoup


def url_bs4(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        demo = r.text
        return BeautifulSoup(demo, "html.parser").prettify()
    except:
        return "出现异常"


if __name__ == '__main__':
    url = "http://python123.io/ws/demo.html"
    soup = url_bs4(url)
    print(soup)
