import requests
import json

url = "https://ptpress.com.cn/masterpiece/getMasterpieceListForPortal"
r = requests.get(url)
# print(type(r.text))
data = json.loads(r.text)
# print(type(data))
print(data)
bookname = [i['bookName'] for i in data['data']]
# print(bookname)

for i in bookname:
    print(i)