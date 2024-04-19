'''支持向量机（SVM）：用于分类和回归任务的监督学习算法，通过找到最优超平面来分割不同类别的数据点。'''
# 导入所需的库
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 加载示例数据集（鸢尾花数据集）
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建支持向量机分类器对象
svm_clf = SVC()

# 使用训练集训练支持向量机模型
svm_clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = svm_clf.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# 打印模型评估结果
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
