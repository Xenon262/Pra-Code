import requests
from lxml import etree
url = 'https://www.bqkan8.com/50_50096/'
r = requests.get(url)
html = etree.HTML(r.text)

print('HTML对象类型：',type(html))
# 输出body节点下的所有div子节点
print('body节点下所有的div子节点：',html.xpath('/html/body/div'))
# 输出body节点下的所有div子孙节点
print('body节点下所有的div子孙节点：',html.xpath('body//div'))
# 输出body节点下的所有子节点
print('body节点下所有的子节点：',html.xpath('body/*'))