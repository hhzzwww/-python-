import pymysql

'''
db = pymysql.connect(host='10.205.0.193',
                     port=3306, user='root', password='infra123456',
                     database='bee-worker', charset="utf8")

cursor = db.cursor()  # 创建游标对象
sql = 'show databases'  # sql语句

cursor.execute(sql)  # 执行sql语句

one = cursor.fetchone()  # 获取一条数据
print('one:', one)

many = cursor.fetchmany(3)  # 获取指定条数的数据，不写默认为1
print('many:', many)

all_data = cursor.fetchall()  # 获取全部数据
print('all:', all_data)

cursor.close()
db.close()  # 关闭数据库连接
'''

# 创建和管理数据库

# 使用游标对象来执行创建和删除数据库的sql语句示例

db = pymysql.connect(host='localhost', port=3306, user='root', password='888888', charset='utfmb4')

cursor = db.cursor()  # 创建游标对象

try:

    sql = 'show databases'
    cursor.execute(sql)
    print('未创建数据库前：',cursor.fetchall())  # 获取创建数据库前全部数据库

    dbname = 'justtest'
    sql = 'create database if not exists %s'%(dbname)   # 创建数据库
    cursor.execute(sql)
    sql = 'show databases'
    cursor.execute(sql)
    print('创建新的数据库后：',cursor.fetchall())  # 获取创建数据库后全部数据库

    sql = 'drop database if exists %s'%(dbname)  # 删除数据库
    cursor.execute(sql)
    sql = 'show databases'
    cursor.execute(sql)
    print('删除新的数据库后：',cursor.fetchall())  # 获取删除数据库后全部数据库

except Exception as e:
    print(e)
    db.rollback()  # 回滚事务

finally:
    cursor.close()
    db.close()  # 关闭数据库连接
