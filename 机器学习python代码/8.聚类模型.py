
'''k-means聚类模型,用于无监督学习中将数据分成不同的群集。'''
# 导入所需的库
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 创建示例数据集（这里使用make_blobs生成随机数据）
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 创建K均值聚类模型对象
kmeans = KMeans(n_clusters=4)

# 使用模型拟合数据
kmeans.fit(X)

# 获取聚类中心点和预测的类别标签
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# 绘制聚类结果
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, edgecolor='k', c='red', label='Centroids')
plt.legend()
plt.show()
