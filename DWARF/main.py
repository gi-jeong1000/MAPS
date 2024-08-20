import random
import pandas as pd
from sklearn.model_selection import train_test_split

import gda
from sklearn.ensemble import RandomForestClassifier
import time

# config 파일 설정
config = {
    'algorithm': 'ID3',
    'max_depth': 3,
    'enableParallelism': False,
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'population_size': 10,
    'generations': 10,
    'visualizing': True,
    'elitism': 2
}

top_features = 11
sa=[]
def main():
    # 데이터 로드
    for i in range(1):
        start = time.time()
        # column names 설정
        column_names = [
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "free sulfur dioxide",
            "total sulfur dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol",
            "Decision"
        ]
        df = pd.read_csv('../data/wine.csv', header=0,
                         names=column_names, skiprows=1)
        print(df.info())

        # Convert all columns to numeric except 'Decision'
        for col in df.columns:
            if col != 'Decision':
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # # ID 칼럼은 분석에서 제외
        # df.drop(columns=['ID'], inplace=True)

        df['Decision'] = df['Decision'].astype('object')

        X = df.drop(columns=['Decision'])
        y = df['Decision']
        # 데이터셋 7:3 분할
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # 피쳐 임포턴스로 컷오프 진행
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(X, y)

        feature_importances = pd.Series(rf.feature_importances_, index=X.columns)
        feature_importances = feature_importances.sort_values(ascending=False)

        print("Feature Importances:")
        print(feature_importances)

        top_n_features = feature_importances.head(top_features).index.tolist()  # Adjust the number of features as needed

        X_top_features = X_train[top_n_features]
        X_test = X_test[top_n_features]

        df_top_features = pd.concat([X_top_features, y], axis=1)
        df_test = pd.concat([X_test, y_test], axis=1)

        # 초기 염색체 생성
        past_population = [
            gda.Chromosome(list(df_top_features.columns), df_top_features, cat_names=[], target='Decision',
                           algorithm=config['algorithm']) for _ in range(config['population_size'])]

        # 유전 알고리즘 수행
        for generation in range(config['generations']):
            print(f"Generation {generation + 1}")

            new_population = past_population

            # 변이 및 교차로 새로운 염색체 생성
            while len(new_population) < config['population_size']:
                parent1 = random.choice(past_population)
                parent2 = random.choice(past_population)
                if random.random() < config['crossover_rate']:
                    offspring = parent1.crossover(parent2)
                else:
                    offspring = parent1.clone()
                if random.random() < config['mutation_rate']:
                    offspring = offspring.mutate()
                new_population.append(offspring)

            # 평가 후 정렬
            evaluated_population = [(individual, individual.evaluate(df_top_features)) for individual in new_population]
            evaluated_population.sort(key=lambda x: x[1], reverse=True)

            # 결과 출력
            best_individual, best_score = evaluated_population[0]
            final_score,precision,recall,f1 = best_individual.final(df_test)
            print(f"Generation {generation} Score: {final_score}")

            # Elitism 적용
            past_population = [individual for individual, _ in evaluated_population[:config['elitism']]]
        end = time.time()
        sa.append([end-start,final_score,precision,recall,f1])
    avg= (sa[0][0]+sa[1][0]+sa[2][0]+sa[3][0]+sa[4][0])/5
    print("Average Time: ",avg)
    print("Average Score: ",(sa[0][1]+sa[1][1]+sa[2][1]+sa[3][1]+sa[4][1])/5)
    # final score가 가장 높은 best_individual 찾기
    best_score = 0
    best_individual = None
    best_time = 0
    for i in range(5):
        if sa[i][1] > best_score:
            best_score = sa[i][1]
            best_time = sa[i][0]
            best_precision = sa[i][2]
            best_recall = sa[i][3]
            best_f1 = sa[i][4]
    print("Best Time: ",best_time)
    print("Best Score: ",best_score)
    print("Best Precision: ",best_precision)
    print("Best Recall: ",best_recall)
    print("Best F1: ",best_f1)

if __name__ == "__main__":
    main()