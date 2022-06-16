import scrapy
from tipdmScrapy1.items import Tipdmscrapy1Item

class SpiderTitleSpider(scrapy.Spider):
    name = 'spider_title'
    allowed_domains = ['www.tipdm.com']
    start_urls = ['http://www.tipdm.com/xwzx/index.jhtml']

    def parse(self, response):
        item = Tipdmscrapy1Item()
        titles = response.xpath('//*[@id="t505"]/div/div[3]/h1/a/text()').extract()
        item['title'] = titles
        return item