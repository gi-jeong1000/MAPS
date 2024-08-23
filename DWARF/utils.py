import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import embedData

def load_data(data:str):
    if data == "wine":
        return embedData.load_wine()
    elif data == "wdbc":
        return embedData.load_wdbc()
    elif data == "Dusan":
        return embedData.load_Dusan()

def cut_off_and_split(X,y, top_features,train_ratio=0.7):
    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-train_ratio)
    # 피쳐 임포턴스로 컷오프 진행
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)

    feature_importances = pd.Series(rf.feature_importances_, index=X_train.columns)
    feature_importances = feature_importances.sort_values(ascending=False)

    print("Feature Importances:")
    print(feature_importances)

    top_n_features = feature_importances.head(top_features).index.tolist()  # Adjust the number of features as needed

    X_top_features = X_train[top_n_features]
    X_test = X_test[top_n_features]

    df_train = pd.concat([X_top_features, y_train], axis=1)
    df_test = pd.concat([X_test, y_test], axis=1)

    return df_train, df_test
