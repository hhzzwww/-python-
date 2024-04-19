'''线性回归模型：用于建模线性关系的模型，例如预测房屋价格等连续数值型数据。'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pickle

data = pd.DataFrame({'x1': [2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2, 2, 1.75, 1.75, 1.75, 1.75, 1.75,
                            1.75, 1.75, 1.75, 1.75, 1.75, 1.75],
                     'x2': [5.3, 5.3, 5.3, 5.3, 5.4, 5.6, 5.5, 5.5, 5.5, 5.6, 5.7, 5.9, 6, 5.9, 5.8, 6.1, 6.2, 6.1, 6.1,
                            6.1, 5.9, 6.2, 6.2, 6.1],
                     'y': [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075, 1047, 965, 943, 958,
                           971, 949, 884, 866, 876, 822, 704, 719]
                     })
print(data.head())

y = data["y"]
X = sm.add_constant(data[["x1", "x2"]])
model = sm.OLS(y, X)
results = model.fit()
results.summary()
print(results.summary())

import matplotlib.pyplot as plt

# 创建一个空白图像
fig, ax = plt.subplots(figsize=(8, 6))

# 将结果摘要文本添加到图像中
text = results.summary().as_text()
ax.text(0.1, 0.5, text, fontsize=10, transform=ax.transAxes)

# 隐藏坐标轴
ax.axis('off')

# 保存图像为PNG文件
plt.savefig('linear_regression_summary.png', bbox_inches='tight', dpi=300)

# 显示图像（可选）
plt.show()
