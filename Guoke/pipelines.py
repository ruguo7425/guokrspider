# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from Guoke.items import GuokeLiItem, GuokeItem

import json


class TencentJsonPipeline(object):
    # 爬虫启动时执行一次
    def open_spider(self, spider):
        self.f = open("GuokeLiItem.json", "w")

    # 必须实现的，用来处理每一个item数据
    def process_item(self, item, spider):
        if isinstance(item, GuokeLiItem):
            content = json.dumps(dict(item, ), ensure_ascii=False) + ",\n"
            self.f.write(content.encode('utf8'))

        return item

    # 爬虫关闭时执行一次
    def close_spider(self, spider):
        self.f.close()


class PositionJsonPipeline(object):
    # 爬虫启动时执行一次
    def open_spider(self, spider):
        self.f = open("GuokeItem.json", "w")

    # 必须实现的，用来处理每一个item数据
    def process_item(self, item, spider):
        if isinstance(item, GuokeItem):
            content = json.dumps(dict(item, ), ensure_ascii=False) + ",\n"
            self.f.write(content.encode('utf8'))

        return item

    # 爬虫关闭时执行一次
    def close_spider(self, spider):
        self.f.close()
