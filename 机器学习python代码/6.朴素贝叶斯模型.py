'''朴素贝叶斯模型：基于贝叶斯定理和特征之间的独立性假设，适用于文本分类和其他特征之间独立的情况。'''
# 导入所需的库
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 加载示例数据集（鸢尾花数据集）
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建高斯朴素贝叶斯分类器对象
gnb = GaussianNB()

# 使用训练集训练朴素贝叶斯模型
gnb.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = gnb.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# 打印模型评估结果
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
