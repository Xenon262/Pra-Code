# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd
class Tipdmscrapy1Pipeline:
    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item))
        data.to_csv('title.csv',encoding='utf-8-sig')