# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/12/13 19:30
# @Author:86151
# @Site:
# @File:7.Numpy与pandas库.py
# @Software:PyCharm

# import pandas as pd
# data = pd.read_excel(r'C:\Users\86151\Desktop\data.xlsx')
# # print(data)
# #
# import pandas as pd
# from pandas import DataFrame
# # # data=pd.read_excel('data.xlsx')
# # # print(data)
#
# data1 = pd.read_excel('data.xlsx',sheetname=0,encoding='utf-8')
# print(data1)

# data =pd.read_csv('data.csv')
# print(data)
# data = pd.read_csv('data.csv',delimiter = ',',encoding='utf-8')
#
# data1 = pd.DataFrame([[1,2],[3,4],[5,6]],columns=['A列','B列'])
# print(data1)
#
# data1.to_excel('data.xlsx')
# data1.to_excel('data.xlsx',columns=['A列'],index=False)
#
# data.to_csv('data.csv')
#
# data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index = ['r1','r2','r3'],columns=['c1','c2','c3'])
# print(data)
#
# b = data.iloc[1:3]
# c = data.iloc[-1]
# print(b)
# print(c)
# d = data.loc[['r2','r3']]
# # print(d)
# e = data.head(2)
# print(e)
# a = data[['c1','c3']][0:2]
# print(a)
# #实战中，通常采用iloc和列读取相结合的方式来读取特定的区块数据
# b = data.iloc[0:2][['c1','c3']]
# print(b)

# data['c4'] = data['c3'] - data['c1']
# data.head()
# print(data)

# a = data[data['c1']>1]
# print(a)
# a = data.sort_values(by = 'c2',ascending = False)
# print(a)
# a = a.sort_index()
# print(a)

# DataFrame.drop(index=None,columns=None,inplace = False)
# a = data.drop(columns ='c1')
# print(a)
#
# df1 = pd.DataFrame({'公司':['万科','阿里','百度'],'分数':[90,95,85]})
# df2 = pd.DataFrame({'公司':['万科','阿里','京东'],'股价':[20,180,30]})
# # print(df1)
# # print(df2)
# # df3 = pd.merge(df1,df2)
# print(df3)
# df4 = pd.merge(df1,df2,how = 'outer')
# print(df4)
#
# df5 = pd.merge(df1,df2,how = 'left')
# print(df5)

# df3 = pd.merge(df1,df2,left_index =True,right_index = True)
# print(df3)

# df3 = pd.concat([df1,df2],axis = 0)
# print(df3)
#
# df3 = pd.concat([df1,df2],ignore_index = True)
# print(df3)
#
# df3 = pd.concat([df1,df2],axis = 1)
# print(df3)
#
# df3 = df1.append(df2)
# print(df3)
#
# df3 = df1.append({'公司':'腾讯','分数':'90'},ignore_index = True)
# print(df3)





#创建数组的几种方式
# import numpy as np
# a = np.array([1,2,3,4])
# b = np.array([1,2],[3,4],[5,6])
# c = np.arange(5,10,0.5)
# d = np.arange(12).reshape(3,4)
# e = np.random.randint(0,10,(4,4))
#

# #DataFrame索引的修改
# import pandas as pd
# a = pd.DataFrame([[1,2],[3,4],[5,6]],columns = ['date','score'],index = ['A','B','C'])
# a.index.name = '公司'
# # print(a)
#
# #将常规列转化为行索引
# import numpy as np
# import pandas as pd
# # #sheetname = 0表示第一个工作表，encoding指定文件编码方式，防止乱码
# # data = pd.read_excel('121.xlsx',sheetname = 0,encoding = 'utf-8')
# #
# # #读取csv格式文件
# # data1 = pd.read_csv('data.csv')
# # #delimiter参数用于指定CSV文件中的分隔符号，默认为逗号；encoding参数用于指定编码方式
# # data2 = pd.read_csv('data.csv',delimiter=',',encoding = 'utf-8')
#
# #数据的读取和编辑
# data =pd.DataFrame(np.arange(1,10).reshape(3,3),index = ['r1','r2','r3'],columns = ['c1','c2','c3'])
# print(data)
#读取的为一维的Series类型的数据
# a = data['c1']
# print(a)
# #读取二维的表格数据
# b = data[['c1']]
# print(b)
# c = data[['c1','c3']]

#按照行读取数据
# a = data[1:3]
# print(a)


# #pandas 土建使用iloc方法来根据行序号读取数据
# b = data.iloc[1:3]

# c = data.iloc[-1]
# print(c)

#通过loc的方法根据行名称读取数据
# d = data.loc[['r2','r3']]9
# print(d)
#
# # e = data.head() #读取前五行
#
# #读取c1和c3的前两行
# a = data[['c1','c3']][0:2]
# print(a)
#
# #实战中通常采取iloc和列读取相结合的方式读取特定的区块数据
# b = data.iloc[0:2][['c1','c2']]
#
# #读取单个值
# d = data.iloc[0]['c3']
#
# #也可以使用loc的方式
# e = data.loc['r1','r2']['c1','c2']
#
# #数据的运算
# data['c4'] = data['c1'] - data['c2']
#
# #数据的筛选
# a = data[data['c1']>1]
#
# g= data[(data['c1']>1) & (data['c2'] ==5)]
#
