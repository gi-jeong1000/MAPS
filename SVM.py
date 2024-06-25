from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from preprocess.ReadData import read_iris_data, read_dusan

# 데이터셋 로드
# data, x_columns, y_column, feature_types = read_iris_data()
data, x_columns, y_column, feature_types = read_dusan()

# 데이터셋 분리는 안함

# 레이블 인코딩
label_encoder = LabelEncoder()
data[y_column] = label_encoder.fit_transform(data[y_column])

# SVM 모델 학습
svm = SVC(kernel='linear')
svm.fit(data[x_columns], data[y_column])

# 정확도, 정밀도, 재현율, F1 점수 출력
accuracy = accuracy_score(data[y_column], svm.predict(data[x_columns]))
precsion = precision_score(data[y_column], svm.predict(data[x_columns]), average='macro')
recall = recall_score(data[y_column], svm.predict(data[x_columns]), average='macro')
f1 = f1_score(data[y_column], svm.predict(data[x_columns]), average='macro')

print("Accuracy:", accuracy)
print("Precision:", precsion)
print("Recall:", recall)
print("F1 Score:", f1)
