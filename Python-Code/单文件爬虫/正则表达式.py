import requests
import re

url ='http://tjsyxy.fanya.chaoxing.com/portal'
r = requests.get(url)

pattern = re.compile('a href=.*?_blank.*?>(.*?)</a>')
items = re.findall(pattern,r.text)

for item in items:
    print(item)