import requests
from bs4 import BeautifulSoup

url = 'http://tjsyxy.fanya.chaoxing.com/portal'
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

print('h3节点内容：',soup.find_all(name = 'h3',limit=3))
print('根据class属性来查找节点',soup.find_all('a',attrs={'class':'Limitlogin'}))
print('通过string参数来查找：',soup.find_all(text = '更多'))