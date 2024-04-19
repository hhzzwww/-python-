'''主要用于二分类问题，可以输出概率值表示属于某一类的概率。'''
# 导入所需的库
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 创建示例数据集（这里使用的是 Scikit-Learn 内置的鸢尾花数据集）
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型对象
logreg = LogisticRegression()

# 使用训练集训练模型
logreg.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = logreg.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# 打印模型评估结果
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
