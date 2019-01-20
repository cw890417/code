import requests
from bs4 import BeautifulSoup


def getHTMLTexr(mn):
    try:
        url = 'http://www.ip138.com:8080/search.asp'
        param = {'mobile': mn, 'action': 'mobile'}
        kv = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3673.0 Safari/537.36'}
        r = requests.get(url, headers=kv, params=param)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def parseText(text):
    soup = BeautifulSoup(text, 'html.parser')
    tables = soup.find_all('table')
    dict = {}
    for i in tables[1].find_all('tr', bgcolor='#EFF1F3'):
        key = i.find('td').text
        val = str(i.find('td', class_='tdc2').text).split(' ')[0]
        dict.update({key: val})
    return dict


if __name__ == '__main__':
    soup = getHTMLTexr('15215155697')
    for k, v in parseText(soup).items():
        print('{0}  {1}'.format(k, v))
