# -*- coding: utf-8 -*-
import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['https://www.goodreads.com/quotes']
    start_urls = ['http://https://www.goodreads.com/quotes/']

    def parse(self, response):
        pass
