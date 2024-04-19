# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2022/1/15 13:47
# @Author:86151
# @Site:
# @File:1.编程规范.py
# @Software:PyCharm

#标识符由 字母，数字，下划线组成，不能以数字开头，习惯性称标识符为变量

# hello_world = 'hello world !'
# my_name = 'huzhiwei'
# print(my_name)

# print 输出函数
#input 输入函数
#当你要的数据需要用户输入的时候，就可以用input()
# your_name = input('请输入你的名字:')
# print(your_name)

# #数值类型
# #整数型
# one = 1
# print(one)
# print(type(one))
#
#
# #float：浮点型,小数
# two = 2.0
# print(two)
# print(type(two))
#
# print(one+two) #输出浮点型’
#
#
# print('------------------')
#
# #数据类型的转换
# print(int(two))
# print(float(one))

#运算符的使用

# three = 3
# ten = 10
#
# #10取余 3 等于1
# print(ten % three) #余数为1
#
# #10取整 3 等于3
# print(ten // three)  #3.33333 取整
#
# print(ten**three)  #10的3次方

# #数字371是不是水仙花数
# number = 371
# a = str(number)[-1]
# b = str(number)[1]
# c = str(number)[0]
# if number == int(a)**3 +int(b)**3 +int(c)**3:
#     print(str(number) +'是水仙花数')
# else:
#     print(str(number) +'不是水仙花数')


# #format占位符
# name = '张三'
# age = 18
# nickname = '法外狂徒'
#
# print('姓名:{},年龄:{},外号:{}'.format(name,age,nickname))
#
# print('-------f 占位符-------')
# print(f'姓名：{name}，年龄：{age}，外号：{nickname}')


#strip、split、replace、join合并
# s = '\n #hello world #\r\n' #\r是换行，\r\n即windows系统下的换行字符
# # print(s.strip())
# # print(s.replace('hello world','你好世界'))
#
# #字符串的链式调用
# print(s.replace('hello','你好').replace('world','世界').strip())
#
# #split------字符串的分隔，默认以空白字符作为分隔符，返回一个列表<数据容器>
# print(s.split())
# print(s.split('#'))
#
#
# s2 ='张三，李四，王五'
# print(s2.split('，'))
# print('?'.join(s2.split('，')))
#
# print(1,2,3,4,sep = ' ')
# print(1,2,3,4,sep = ',')


# number = 371
# print(str(number)[0])
#
#
# name = '张三'
# age = 18
# nickname = '法外狂徒'
#
# print(f'姓名：{name}，年龄：{age}，外号：{nickname}')
#
#split分割后是列表
#join添加后为字符串
#
# flag = 'hello'
# if flag:  #bool值的隐式转换
#     print('猜下我会打印吗')


'''
#is 身份运算
names = ['正心','丸子','山禾']
name = '正心'
print('正心' in names)


#if
# 对于已知的东西，全部用if、elif，只有对未知的东西才用else


index = 1
while index <=100:
    print('我爱python' + str(index))
    index +=1

'''
#
# row = 1
# while row <= 9:
#     col = 1
#     while col <=row:
#         print(f'{row} * {col} = {row*col}',end = ' ')
#         col +=1
#     print()
#     row += 1

# index = 5
# for row in range(1, index + 1, 1):
#     # print('*')
#     for col in range(1, row + 1, 1):
#         print('*', end='')
#     print()

# pwd = '123456'
# count = 1
# # 不清楚 while 循环需要执行多少次的时候，直接给死循环
# while True:
#     entry_password = input('请输入密码：')
#     count += 1
#     if entry_password == pwd:
#         print('密码输入正确，登录成功')
#         break  # 遇到 break 的时候就会结束循环
#
#     if count > 3:
#         print('密码输入错误，账号已经锁死')
#         break
#     print(f'密码输入错误，请重新输入（第{count - 1}次）')
#
# print('登录成功，请选择操作：（1）：取钱 （2）:存钱')
'''

pwd = '123456'
count = 1
while True:
    entry_password = input('请输入密码：')
    count += 1

    if entry_password ==pwd:
        print('密码输入正确，登录成功')
        break
    if count > 3:
        print('密码输入错误，账号已经锁死')
        break
    else:
        print(f'密码输入错误，请重新输入（第{count - 1}次）')

print('登录成功，请选择操作：（1）：取钱 （2）:存钱')


'''
'''

extend 将一个列表合并到另一个列表  arr3自己也是列表
insert 将制定元素插入列表 arr.insert(0,'自游')


列表的使用方法
添加 append、extend、合并--‘+’、insert--list.insert(索引, 元素) 插入元素到指定索引的前面
删除 pop、remove
查询索引元素的位置  index
查询元素出现的次数  count

元组的使用方法--元组不可修改，故只有查询功能
查询索引元素的位置 index
查询元素出现的次数 count
'''
"""
    基本的数据类型：int float str bool
    基本的数据容器：list、tuple、set、dict

one = 1
print(bool(one))
print(str(one))
print(float(one))

string = '5'  # 字符串转化为数值类型需要满足一定条件
print(int(string))

# 数据容器的转化
string = 'hello'
print(list(string))
print(tuple(string))
arr = ['h', 'e', 'l', 'l', 'o']
print(str(arr))
# 容器转化为字符串，需要满足一定条件
print(''.join(tuple(arr)))

arr2 = [1, 2, 3, 4, 5]
# 列表里面的数字无法直接用join
for index in range(len(arr2)):
    arr2[index] = str(arr2[index])
print(''.join(arr2))
"""

'''
位置参数
默认参数
关键字参数
*args
**args


'''


'''
文件读取
line = file.readlines()----表示一行行读取所有内容，返回是一个列表

line1 = file.readline()---表示一次读取一行数据

二进制数据操作：
    保存二进制的文本
    message = '世界你好'
    二进制编码-----------content = message.encode('utf-8')
    二进制解码-----------content = message.decode('utf-8')
    
    字符串--》 编码为二进制的内容 --》wb 方式保存 --》wr 方式读取--》把字符串解码为字符串
             图片二进制的内容---》 wb 方式保存 --》 wb 方式读取
    
    encoding：文字类的东西都会有编码
    二进制内容没有编码：图片/excel/pdf/mp3/mp4
    
    后缀：操作系统的拓展，帮助系统使用正确的软件读取文件
    
    
'''
'''
类与对象
1.将类对象的概念抽象出来---class Hero:
2.在初始化方法中，进行抽象对象的属性初始化操作---def__init__(self)
#self 是实例对象
#javascript,java 是隐式的this，在python里面是显示的self
3.将对象的行为--实现---def eat():

类与对象---对象有属性（姓名、身高、体重、年龄）和方法（吃、喝、玩、乐）
  
'''
'''
类与继承
#继承：子类默认继承父类所有的属性和方法
#父类不可以调用子类的属性和方法

'''



















