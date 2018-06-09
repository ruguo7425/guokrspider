# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuokeItem(scrapy.Item):
    # define the fields for your item here like:
    # 关注人数
    Attention_degree = scrapy.Field()
    # 回答人数
    Answer = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 标题url
    title_url = scrapy.Field()


class GuokeLiItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 详情内容
    details = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 回到内容
    content = scrapy.Field()
