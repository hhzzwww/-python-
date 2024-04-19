# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/12/19 12:28
# @Author:86151
# @Site:
# @File:5.Python与Mysql数据库的交互.py
# @Software:PyCharm


# # #先预定义一些变量
# company = '阿里巴巴'
# title = '测试标题'
# href = '测试链接'
# source = '测试来源'
# date = '测试日期'

# company = '阿里巴巴'
# title = '标题1'
# href = '链接1'
# source = '来源1'
# date = '日期1'

#连接到数据库
# import pymysql
# #host:Mysql服务地址； port:端口； charest:编码方式，和之前的utf-8不同，中间少了‘-’ database:连接到的数据库名称
# db = pymysql.connect(host='localhost',port=3306,user = 'root',password='',database='pacong1',charset='utf8')
#
# #插入数据
# cur = db.cursor() #获取会话指针，用来调用sql语句
# #%s表示占位符(字符串类型）,整数类型为%d，小数类型为%f，可以批量插入多家公司信息#编写sql语句
# sql = 'INSERT INTO test(company,title,href,date,source) VALUES(%s,%s,%s,%s,%s)'
# cur.execute(sql,(company,title,href,date,source)) #execute用于执行SQL语句并传入相应内容 execute:执行
# db.commit() #commit更新数据表的固定写法，commit:提交
# cur.close()#关闭会话指针
# db.close()#关闭数据库连接
# # #

# b = '我的名字时%s,我的岁数是%d' %('华小智',25)
# print(b)


#用python在数据库中查找并提取数据
# import pymysql
# db = pymysql.connect(host = 'localhost',port=3306, user = 'root',password = '',database = 'pacong1',charset = 'utf8')
#
# company = '阿里巴巴'
# title = '链接1'
#
# cur = db.cursor()
# sql = 'SELECT * FROM test WHERE company =%s'
# cur.execute(sql,company)#执行sql语句
# data = cur.fetchall() #提取所有数据，并赋值给变量data
# print(data)
# db.commit() #提交修改，这一行其实可以不写，因为没有改变数据表的结构
# cur.close()
# db.close()
#
# #将数据库中的信息定位提取出来
# for i in range(len(data)):
#     print(data[i][1])
#
# #在多个筛选条件下提取数据
# sql = 'SELECT * FROM test WHERE company =%s AND title = %s'
# cur.execute(sql,(company,title))


# #用python从数据库中删除数据
# import pymysql
# db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password='',database = 'pacong1',charset = 'utf8')
#
# company = '阿里巴巴'
#
# cur = db.cursor()
# sql ='DELETE FROM test WHERE company  =%s'
# cur.execute(sql,company)
# db.commit()
# cur.close()
# db.close()



#案例实战：把金融数据存入数据库
import requests
import re
import pymysql

headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53'}

def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company
    res = requests.get(url,headers = headers).text

#正则提取
    p_source = ' <span class="c-color-gray c-font-normal c-gap-right" aria-label=".*?">(.*?)</span>'
    source = re.findall(p_source,res,re.S)

    p_date = '<span class="c-color-gray2 c-font-normal" aria-label=".*?">(.*?)</span>'
    date = re.findall(p_date,res)

    p_href ='<h3 class="news-title_1YtI1"><a href="(.*?)"'
    href = re.findall(p_href,res)

    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a></h3>'
    title = re.findall(p_title, res, re.S)

#数据清洗
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])


#生成txt文件文本
    # file1 = open(r'C:\Users\86151\Desktop\\数据挖掘报告.txt', 'a',encoding='utf-8')
    # file1.write(company + '数据挖掘completed!' + '\n' + '\n')
    # for i in range(len(source)):
    #     file1.write(str(i+1) + '.' + title[i] + '(' + date[i] + '_' + source[i] + ')' + '\n')
    #     file1.write(href[i] + '\n')
    # file1.write('------------------------------' + '\n' + '\n')
    # file1.close()


#将爬取的数据导入mysql数据库
    for i in range(len(source)):
        db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password='',database = 'pacong1',charset = 'utf8')

        cur = db.cursor()
        sql = 'INSERT INTO test(company,title,href,date,source)VALUES(%s,%s,%s,%s,%s)'
        cur.execute(sql,(company,title[i],href[i],date[i],source[i]))
        db.commit()
        cur.close()
        db.close()
#
# baidu('阿里巴巴')

#批量爬取多家公司的信息并把它们存入数据库
companys =['华能信托','阿里巴巴','万科集团','百度','腾讯','京东']
for company in companys:
    try:
        baidu(company)
        print(company + '爬取数据并存入数据库成功')
    except:
        print(company + '爬取数据并存入数据库失败')










































