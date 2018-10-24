# -*- coding: utf-8 -*-
import scrapy


class ExpampleSpider(scrapy.Spider):
    name = 'expample'
    allowed_domains = ['http://web.catedu.es/webcatedu/']
    start_urls = ['http://http://web.catedu.es/webcatedu//']

    def parse(self, response):
        pass
