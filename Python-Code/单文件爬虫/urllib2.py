import urllib.request

url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {'i': '香蕉',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16474052686702',
    'sign': '75b024d2a49fe8711cb8ac48bfd043a4',
    'lts': '1647405268670',
    'bv': 'cdd63870d07eb5030b9324cc7f7de35b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data=data)
print(response.read().decode('utf-8'))