# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from Guoke.items import GuokeItem, GuokeLiItem


class GuokeSpider(CrawlSpider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/?page=1']
    """
    https://www.guokr.com/ask/highlight/?page=7
    "/ask/highlight/?page=7"
    "/ask/highlight/?page=5"
    
    "https://www.guokr.com/question/652161/"
    "https://www.guokr.com/question/652049/"
    """
    rules = [
        Rule(LinkExtractor(allow=r'/ask/highlight/\?page=\d+'), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=r'https://www.guokr\.com/question/\d+'), callback='parse_data', follow=False)
    ]

    def parse_page(self, response):
        lis = response.xpath('//ul[@class="ask-list-cp"]/li')
        for i in lis:
            item = GuokeItem()
            item['Attention_degree'] = i.xpath('./div[1]/p[1]/span/text()').extract_first()
            item['Answer'] = i.xpath('./div[1]/p[2]/span/text()').extract_first()
            item['title'] = i.xpath('./div[2]/h2/a/text()').extract_first()
            item['title_url'] = i.xpath('./div[2]/h2/a/@href').extract_first()
            yield item

    def parse_data(self, response):
        item = GuokeLiItem()
        item['title'] = "\n".join(response.xpath('//h1[@id="articleTitle"]/text()').extract())
        item['details'] = "\n".join(response.xpath("//*[@id='questionDesc']/p[1]/text()").extract())
        item['name'] = "\n".join(
            response.xpath("//*[@id='answer860412']/div[2]/div[1]/p/text()").extract())
        item['content'] = "\n".join(response.xpath("//*[@id='answer860412']/div[2]/div[3]/p/text()"))
        yield item
