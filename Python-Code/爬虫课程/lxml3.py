import requests
from lxml import etree


url = 'https://www.bqkan8.com/50_50096/18520412.html'

r = requests.get(url)
html = etree.HTML(r.text)

title = html.xpath('//h1/text()')[0]
print(title)
contents = html.xpath('//div[@id="content"]/text()')
for i in contents:
    content = i.strip()
    print(content)