# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class AixiashuPipeline:
    def __init__(self):
        self.file = open('book.json','w')

    def process_item(self, item, spider):
        item=dict(item)
        # item['content'] = item['content'].split('\xa0\xa0\xa0\xa0')[1]
        json_data = json.dumps(item,ensure_ascii=False) + ', \n'
        self.file.write(json_data)
        return item
    def __del__(self):
        self.file.close()

