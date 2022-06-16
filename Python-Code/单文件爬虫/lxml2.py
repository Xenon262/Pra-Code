from turtle import ht
import requests
from lxml import etree

url = 'https://www.bqkan8.com/50_50096/18520412.html'

r = requests.get(url)

html = etree.HTML(r.text)
print('class属性为content的div节点：',html.xpath('//div[@class="content"]'))
print('id属性值包含tent的div节点：',html.xpath('//div[contains(@id,"tent")]'))
print('id属性值为content的div节点的class属性值：',html.xpath('//div[@id="content"]/@class'))