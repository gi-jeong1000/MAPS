import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 데이터셋 로드
column_names = [
    'ID', 'Diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
    'concave_points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
    'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst',
    'symmetry_worst', 'fractal_dimension_worst'
]
df = pd.read_csv('../data/wdbc.data', header=None, names=column_names)

# 타겟 열 'Decision'으로 이름 변경
df.rename(columns={'Diagnosis': 'Decision'}, inplace=True)

# 타겟 열을 'object' 타입으로 변환
df['Decision'] = df['Decision'].astype('object')

# ID 열 제거
df.drop(columns=['ID'], inplace=True)

# 특성과 타겟 분리
X = df.drop(columns=['Decision'])
y = df['Decision']

# 의사결정 나무 모델 생성 및 학습
clf = DecisionTreeClassifier(random_state=42, max_depth=5)
clf.fit(X, y)

# 학습 데이터로 평가
y_pred = clf.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy}")

# 트리 시각화
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=y.unique(), filled=True)
plt.show()