import scrapy

'''
爬虫文件：
    1.收集需要采集的网址
    2.解析数据
'''


# scrapy.Spider 爬虫基类
class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # 爬虫文件的名字---创建文件时自己指定的名字，后期启动爬虫项目时需要指定爬虫名字
    # allowed_domains = ['toscrapy.com']  # 限制我们抓取网址时的域名
    allowed_domains = []  # 不指定域名
    # 采集数据的起始网址， 通过 genspider 自动生成的，一般是错误的，需要修改
    # 对于有规律的url地址，一般采用列表推导式收集所有需要采集的地址
    # start_urls = ['http://quotes.toscrape.com/']

    # 重写start_urls
    def start_requests(self):
        yield scrapy.Request(url='http://quotes.toscrape.com/', callback=self.parse)

    def parse(self, response):
        # start_urls    起始网址返回的数据，默认会给 parse 函数进行处理
        # parse 函数必须列带 response
        # response 具有所有响应体的方法和属性 + 也具有 parsel 模块中所有数据解析的方法<css,xpath,re>

        """采用数据二次提取的方式"""
        divs = response.css('.quote')
        for div in divs:
            text = div.css(' .text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()
            # print(text, author, tags)
            # 如果获取的数据，是通过yield返回的是一个字典，那么scrapy框架会自动处理
            # scrapy框架里面所有爬虫文件按返回的数据 全部用yield返回
            # yield 一条一条的返回数据内容

            yield {'text': text, 'author': author, 'tags': tags}
        # print(response.text)
        # 处理翻页
        next_page = response.css('.next>a::attr(href)').get()  # 下一页部分地址
        if next_page:
            all_url = 'https://quotes.toscrape.com' + next_page  # 完整地址
            # scrapy.Request  构建一个requests请求，让下载中间件进行下载，也会返回部分地址
            # callback 参数就是指定当前的请求要交给那个函数做处理，回调函数
            yield scrapy.Request(url=all_url, callback=self.parse)

        pass


'''
如何处理反扒？
如何保存数据？
如何知道框架底层调度流程？
'''
