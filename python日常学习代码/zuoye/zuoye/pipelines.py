# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter

# class ZuoyePipeline:
#     # process_item 主要写入数据的方法， item 可以获取流经管道的数据
#     def process_item(self, item, spider):
#         print('管道文件打印数据：', item)
#         d = dict(item)
#         with open('zuoye1.csv', mode='a', encoding='utf-8') as f:
#             f.write(d['title1'] + ',' + d['blank'] + ',' + d['href'])
#             f.write('\n')
#
#         return item


''' 创建一次'''
# 1.创建工作簿对象
# 2.创建表

'''操作多次'''
# 3.表写入数据
''' 操作一次'''


# 4.保存工作簿

import json
class CsvPipeline:
    def __init__(self):
        # 初始化方法，一般打开文件，数据库对象
        self.f = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title1', 'blank', 'href'])
        self.csv_write.writeheader()  # 写表头，只需要写入一次
        pass

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        pass

    def process_item(self, item, spider):
        self.csv_write.writerow(item)  # 把item数据一条一条写入

        """
        :param item: 爬虫文件返回的一条一条数据
        :param spider:区分爬虫对象的参数
        :return:返回一条一条数据，必须原路返回，可以便于下一个管道类使用
        """
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline 组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        return item  # 将数据返回，可能供其他的管道类使用

    def close_spider(self, spider):
        """整个项目停止前会调用的方法，一般用于关闭文件，关闭数据连接"""
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        self.f.close()
        pass


# json数据结构 ---->[{},{},{},.....]
class JsonPipeline:
    def open_spider(self, spider):
        self.f = open('english.json', mode='w', encoding='utf-8')
        self.d_list = []  # 用于收集每一天数据，构建json结构

    def process_item(self, item, spider):
        d = dict(item) # 针对json数据需要把item强制转化成原生的字典对象
        self.d_list.append(d)
        return item
        pass

    def close_spider(self, spider):
        # 执行json数据序列化操作
        json_str = json.dumps(self.d_list, ensure_ascii=False)
        self.f.write(json_str)
        self.f.close()

        pass

