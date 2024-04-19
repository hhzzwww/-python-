import scrapy
from ..items import Qd01QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes_items'

    allowed_domains = []
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        divs = response.css('.quote')

        for div in divs:
            text = div.css(' .text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()
            yield Qd01QuotesItem(text=text, author=author, tags=tags)

        # print(response.text)
        pass
