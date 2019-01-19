from urllib.request import *

with urlopen('http://www.baidu.com') as f:
    data = f.read()
    print(data.decode('utf-8'))
