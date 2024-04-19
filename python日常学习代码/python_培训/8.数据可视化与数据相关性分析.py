# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/12/13 21:17
# @Author:86151
# @Site:
# @File:8.数据可视化与数据相关性分析.py
# @Software:PyCharm


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([1,2,3])
# y1 = x*2
# y2 = x+1
# #color设置颜色，linewidth设置线宽，单位为像素；linestyle设置线型，默认为实线
# #第一条线：设置label(标签)为'y = x*2'
# plt.plot(x,y1,color = 'grey',linewidth = 1,linestyle = '--',label = 'y = x*2')
# plt.plot(x,y2,color = 'red',linewidth = 1,label = 'y = x+1')
# #显示标题
# plt.title('Hello')
# #显示x轴
# plt.xlabel('x')
# #显示y轴
# plt.ylabel('Y')
# #设置图例位置为左上角,lower right为右下角
# plt.legend(loc = 'upper left')
# plt.show()

#设置双坐标
# # plt.twinx()
#
# import matplotlib.pyplot as plt
# import numpy as np
# #设置第一条线的label为y =x
# x1 = np.array([10,20,30])
# y1 = x1
# plt.plot(x1,y1,color = 'grey',linestyle = '--',label = 'y=x')
# plt.legend(loc = 'upper left')#设置该图表图例在左上角
#
# plt.twinx() #设置双坐标
# y2 = x1*x1
# plt.plot(x1,y2,label = 'y2=x^2')
# plt.legend(loc = 'upper right')#设置该图表图例在右上角
# #设置图表大小
# plt.rcParams['figure.figsize'] = (8,6)
#
# plt.show()
#
# #解决中文显示问题
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #解决负号显示为方块的问题




#数据可视化实战
# import datetime
# import pandas as pd
# import matplotlib.pyplot as plt
# score = pd.read_excel('score.xlsx')
# share = pd.read_excel('share.xlsx')
# share = share[['date','close']]
# #on 表示按照日期进行合并 how = 'inner'表示取交集
# data = pd.merge(score,share,on = 'date',how = 'inner') #数据合并
# #merge()函数默认按公共列以取交集的方式连接
# # data1 = pd.merge(score,share)
# # print(data)
# # #将data中的数据写入excel
# # data.to_excel('data.xlsx')
#
# import datetime
# import pandas as pd
# import matplotlib.pyplot as plt
# #设置中文字体格式为黑体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# data = pd.read_excel('data.xlsx')
#
# #把日期由由string类型转为Timestamp类型，方便刻度显示
# d = []
# for i in range(len(data)):
#     d.append(datetime.datetime.strptime(data['date'][i],'%Y-%m-%d'))
# data['date'] = d #将原来的date那一列数据换成新生成的时间戳格式日期
#
#
# #数据可视化并设置双坐标轴
# plt.plot(data['date'],data['score'],linestyle = '--',color = 'grey',label = '评分')
# #设置X轴刻度显示角度
# plt.xticks(rotation = 45)
# #设置评分的图例显示在左上角
# plt.legend(loc = 'upper left')
# #设置双坐标轴
# plt.twinx()
# plt.plot(data['date'],data['close'],label = '股价')
# plt.xticks(rotation = 45)
# plt.legend(loc = 'upper right')
# plt.title('评分对股价趋势影响图')
# plt.show()
#其中data['date']是String类型，如果直接用来描绘图表，x轴坐标会很密集，影响美观，
# 所以这里通过datetime.datetimestrptime()函数将data['date']转化为Timestamp类型，此时Matplotlib库会自动间隔显示



# #相关性分析
# from scipy.stats import pearsonr
# corr = pearsonr(x,y)

# import random
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0,10,0.2)
# y1 = 3*x +5
#
# #y2在y1的基础上机型-5~5之间的随机实数波动
# y2 = []
# for i in y1:
#     y2.append(i + random.uniform(-5,5))
#
# plt.plot(x,y1,color = 'r',label = 'y1')
# plt.plot(x,y2,color = 'grey',label = 'y2')
# plt.legend(loc = 'upper left')
# # plt.show()
#
# #引入SciPy库计算皮尔逊相关系数，代码如下：
# from scipy.stats import pearsonr
# corr = pearsonr(y1,y2)
# print('相关系数r值为' + str(corr[0]) +',显著性水平P值为' + str(corr[1]))

from scipy.stats import pearsonr
import pandas as pd
data = pd.read_excel('data.xlsx')
#相关性分析
corr = pearsonr(data['score'],data['close'])
print('相关系数r值为' + str(corr[0]) +',显著性水平P值为' + str(corr[1]))










