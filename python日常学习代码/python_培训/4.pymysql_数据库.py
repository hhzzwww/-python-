# -*- codeing = Utf-8 -*-
# @Time :2022/2/23 17:02
# @Author :ZunKki
# @File :4.pymysql_数据库.py
# @Software: PyCharm
"""
数据库
"""
'''
# 导入 pymysql 连接数据库
import pymysql

# 1.创建链接对象
connection = pymysql.connect(
    host='159.75.114.202',  # 数据库服务器的地址
    user='windows',  # 用户名
    password='123456',  # 用户密码
    database='hzw_18080008',  # 操作的数据库
    port=3306  # 端口
)
print('链接对象：', connection)

# 2.获取游标对象(执行sql 指令)
# 并发情况下,可以使用多个游标对象,防止相互影响 ---多线程
cursor1 = connection.cursor()  # 做事的人
cursor2 = connection.cursor()  # 做事的人

# 3.执行 sql 执行 -----返回的是生成器
sql = 'show databases;'
count = cursor.execute(sql) -- 执行sql
print('执行sql之后，受影响的行数：', count)

# 4. 获取查询结果
cursor1、cursor2并发执行，防止相互影响
--------------------------------------------
results = cursor1.fetchall()  -- 获取所有的数据
print('cursor2.fetchone()')  -- 获取一条数据
---------------------------------------------
print('cursor.fetchmany(5)') --- 查询5条数据
print('查询结果：', results)
for result in results:
    print(result[0])

# 5. 关闭与服务器的链接
cursor.close()
connection.close()

'''
# 插入 jd_data 数据,案例 -----事务
import pymysql

connection = pymysql.connect(
    host='159.75.114.202',  # 数据库服务器的地址
    user='windows',  # 用户名
    password='123456',  # 用户密码
    database='hzw_18080008',  # 操作的数据库
    port=3306  # 端口
)

cursor = connection.cursor()  # 做事的人

with open('jd_data.csv', mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # lines 为列表
    # print(type(lines))
    for line in lines[:20]:
        try:
            jd = tuple(line.strip().split(','))
            print(jd)

            insert_sql_template = "insert into jd (name,price,commit,shop_name) value('%s','%s','%s','%s');"
            # print(insert_sql_template % jd)

            count = cursor.execute(insert_sql_template % jd)  # 执行sql语句
            # print('执行sql之后，受影响的行数：', count)
            connection.commit()  # 插入成功后立即进行提交 # 提交，不然不回显示数据
        except Exception as e:
            # 如果出错了就全部提交
            print('出错了')
            connection.rollback()  # 回滚,如果发生错误,18种同系物则撤销没有保存到本地的提交--防止出错后还有数据保存在数据库中

cursor.close()
# --关闭数据库
connection.close()
