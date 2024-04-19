import scrapy

from ..items import ZuoyeItem


class Zuoye1Spider(scrapy.Spider):
    name = 'zuoye1'
    allowed_domains = ['language.chinadaily.com.cn']
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]

    def parse(self, response):
        # print(response.text)
        gy_box_txts = response.css('.gy_box_txt')
        for gy_box_txt in gy_box_txts:
            title = gy_box_txt.css('p:nth-child(1)>a::text').get()
            title1 = title.replace('"', '').replace('\n', '')
            blank = gy_box_txt.css('p:nth-child(2)>a::text').get()
            href = gy_box_txt.css('p:nth-child(1)>a::attr(href)').get()
            yield ZuoyeItem(title1=title1, blank=blank, href=href)

        pass











