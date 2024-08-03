import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_wine

# 와인 데이터셋 로드
wine = load_wine()
data = pd.DataFrame(wine.data, columns=wine.feature_names)
data['target'] = wine.target

# 특징 열과 타겟 열 지정
x_columns = wine.feature_names
y_column = 'target'

# 의사결정나무 모델 학습
dt = DecisionTreeClassifier(max_depth=3)
dt.fit(data[x_columns], data[y_column])

# 랜덤 포레스트 모델 학습
rf = RandomForestClassifier(n_estimators=100, max_depth=3)
rf.fit(data[x_columns], data[y_column])

# 정확도 측정
print("Decision Tree Accuracy:", accuracy_score(data[y_column], dt.predict(data[x_columns])))
print("Random Forest Accuracy:", accuracy_score(data[y_column], rf.predict(data[x_columns])))

# 랜덤 포레스트의 특성 중요도 출력
print("Feature Importances:")
for name, importance in zip(x_columns, rf.feature_importances_):
    print(name, importance)

# 랜덤 포레스트 accuracy, precision, recall, f1 score 출력
accuracy = accuracy_score(data[y_column], rf.predict(data[x_columns]))
precision = precision_score(data[y_column], rf.predict(data[x_columns]), average='macro')
recall = recall_score(data[y_column], rf.predict(data[x_columns]), average='macro')
f1 = f1_score(data[y_column], rf.predict(data[x_columns]), average='macro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)