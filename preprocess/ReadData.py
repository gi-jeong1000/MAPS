import pandas as pd
from sklearn.datasets import load_iris


def read_iris_data():
    iris = load_iris()
    # Iris 데이터셋을 DataFrame으로 변환
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    # 클래스 레이블을 문자열로 변환하여 새로운 컬럼에 할당
    data['class'] = [iris.target_names[i] for i in iris.target]

    y_column = 'class'
    feature_types = ['float'] * 4  # 모든 특성은 실수형 데이터
    x_columns = iris.feature_names

    return data, x_columns, y_column, feature_types

def read_dusan():
    x_columns = ['Data' + str(i + 1) for i in range(15)]
    y_column = 'Decision'

    path = 'data/Dusan.csv'
    data = pd.read_csv(path)

    data = data.iloc[:, -16:]
    data.columns = x_columns + [y_column]

    for col in x_columns:
        data[col] = data[col].astype(str).str.replace(',', '').astype(float)

    feature_types = ['float'] * len(x_columns)

    return data, x_columns, y_column, feature_types