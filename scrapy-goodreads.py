import scrapy


class GoodReadsSpider(scrapy.Spider):
    #identity
    name="goodreads"

    def start_requests(self):
        start_urls= 'https://www.goodreads.com/quotes?page=1'
        yield scrapy.Requests(url=url, callback=self.parse)

    #Response
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            print('Texto: ', quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first())
            # print('author', ".//div[@class='quoteText']/child::a")
            # print('tags', ".//div[@class='greyText smallText left']/a")
            