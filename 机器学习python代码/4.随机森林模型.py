'''随机森林模型：由多个决策树组成的集成模型，通过投票或平均预测结果来提高模型的稳定性和准确性。'''
# 导入所需的库
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 加载示例数据集（鸢尾花数据集）
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 目标变量

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建随机森林分类器对象
rf_clf = RandomForestClassifier()

# 使用训练集训练随机森林模型
rf_clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = rf_clf.predict(X_test)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# 打印模型评估结果
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
