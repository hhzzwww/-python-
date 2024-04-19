# # -*- codeing = Utf-8 -*-
'# '# @Time '':''2023/5/17 15:33',',
'# '# @Author '':''ZunKki',',
'# '# @File '':''scrapy框架学习.py',',
'# '# @Software'':'' PyCharm',',

"""
模块：
1.找数据地址
2.请求数据 -- requests、https、urllib模块
3.解析数据 -- css xpath re bs4 lxml 模块
4.保存数据 -- json、csv、openpyxl、pymysql 模块

模块一般来说只能解决某一个需求
"""
'''
框架： 一般是解决某一个需求的一整套方案
    scrapy pyspider等

用scrapy抓取，一般情况下只需要注重爬虫的业务逻辑
需要学习框架特定的语法和一些功能

优点：1.只需要注重爬虫的业务逻辑，一般不需要注重爬虫采集过程中的对象类型
     2.速度会比较快，底层是基于异步的方式实现
     3.可以重写，变化程度大
'''

'''
scrapy 编写流程
01 创建项目
    # 1.创建一个爬虫项目
    scrapy startproject +(项目名字<独一无二>)

    # 2.cd 切换到爬虫项目目录

    # 3.创建爬虫文件
    scrapy genspider (+爬虫文件的名字<独一无二的>) (+域名限制)

02 爬虫文件

    # 1. 修改数据起始地址
    # 2. 写解析数据的业务逻辑

03 爬虫逻辑的编写
    001
        在 settings.py 文件中关闭robots协议
    002
        在爬虫文件下修改起始网址
        在 parse 方法下面解析数据
    003
        在 items.py 文件中定义数据结构
    004
        在 pipelines.py 文件中写保存数据的逻辑
    005
        在 settings.py 配置文件中打开管道配置

04 执行项目
    scrapy crawl +(爬虫文件名字)
'''






























