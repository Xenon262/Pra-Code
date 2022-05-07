import requests
from bs4 import BeautifulSoup

url = 'https://beijing.qfang.com/newhouse'
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

print('soup类型：',type(soup))
print('第一个a节点：',soup.a)
print('a节点类型：',type(soup.a))
print('a节点名字：',soup.a.name)
print('a节点内容：',soup.a.contents)
print('a节点属性：',soup.a.attrs['href'])
print('a节点的string属性：',soup.a.string)