import pandas as pd

def load_wine():
    # CSV 파일을 로드하고 첫 번째 행을 데이터로 사용 (헤더 없이 읽기)
    df = pd.read_csv('../data/wine.csv', header=None)

    # 첫 번째 행을 컬럼 이름으로 설정
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    # 모든 칼럼을 numeric으로 변환, Decision 칼럼 제외
    df = df.apply(pd.to_numeric, errors='ignore')

    # 'Decision' 칼럼을 object로 변환
    df['Decision'] = df['Decision'].astype('object')

    # X와 y 분리 (Decision을 타겟 변수로 설정)
    X = df.drop(columns=['Decision'])
    y = df['Decision']

    return X,y

def load_wdbc():
    # column names 설정
    column_names = [
        'ID', 'Decision', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
        'concave_points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
        'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
        'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]
    df = pd.read_csv('../data/wdbc.data', header=None, names=column_names)

    # ID 칼럼은 분석에서 제외
    df.drop(columns=['ID'], inplace=True)


    X = df.drop(columns=['Decision'])
    y = df['Decision']


    return X,y

def load_Dusan():
    # 데이터셋 로드
    df = pd.read_csv('../data/Dusan.csv')
    # X와 y 분리 (Data1부터 Data15까지가 X, Decision이 y)
    X = df[['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7',
            'Data8', 'Data9', 'Data10', 'Data11', 'Data12', 'Data13', 'Data14', 'Data15']]

    # X 데이터프레임의 모든 열을 숫자형으로 변환
    X = X.apply(pd.to_numeric, errors='coerce')

    # y 열을 object 타입으로 변환 (이산형)
    y = df[['Decision']].astype('object')
    print(y.info())

    return X, y