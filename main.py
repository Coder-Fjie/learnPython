import requests
url = "https://top.jd.com/?cateId=828&itemId=100004325476"
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/69.0.3497.100 Safari/537.36',
           'Referer': 'https://www.baidu.com/'}
try:
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    #查看状态信息，返回的是200，说明返回信息正确并且已经获得该链接相应内容。
    r.encoding = r.apparent_encoding
    #查看编码格式，这个格式是jbk，说明我们从http的头部分已经可以解析出网站信息。
    print(r.text)
except:
    print("爬取失败")