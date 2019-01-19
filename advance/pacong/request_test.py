import requests


def get_request(url):
    """
    获取资源的基础框架
    get资源
    raise检查状态
    encoding编码
    :param url:资源路径
    :return:资源内容
    """
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        # 通过设置user-agent解除爬取限制
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "出现异常"


if __name__ == '__main__':
    url = 'https://www.amazon.cn/dp/B07MPK2DPK'
    print(get_request(url))
