# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from tencent.items import TencentItem

from tencent.items import TencentItem2


class TencentPipeline(object):
    def __init__(self):
        self.file = open('tencent1.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()


class TencentPipeline2(object):
    def __init__(self):
        self.file = open('tencent2.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem2):
            str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()
