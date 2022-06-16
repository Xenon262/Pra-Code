import requests

try:
    r = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png',timeout=1)
except requests.Timeout:
    print('Timeout!')
else:
    print (r.status_code)
print(r.content)

with open('百度.jpg','wb') as f:
    f.write(r.content)