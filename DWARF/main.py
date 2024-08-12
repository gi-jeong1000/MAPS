import random
import pandas as pd
import gda
from sklearn.ensemble import RandomForestClassifier
import time

# config 파일 설정
config = {
    'algorithm': 'CART',
    'max_depth': 5,
    'enableParallelism': False,
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'population_size': 10,
    'generations': 10,
    'visualizing': True,
    'elitism': 2
}

top_features = 7
sa=[]
def main():
    # 데이터 로드
    for i in range(5):
        start = time.time()
        column_names = [
            'ID', 'Diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
            'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
            'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
            'concave_points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
            'perimeter_worst',
            'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst',
            'symmetry_worst', 'fractal_dimension_worst'
        ]
        df = pd.read_csv('../data/wdbc.data', header=None, names=column_names)

        # ID 칼럼은 분석에서 제외
        df.drop(columns=['ID'], inplace=True)

        df['Diagnosis'] = df['Diagnosis'].astype('object')

        X = df.drop(columns=['Diagnosis'])
        y = df['Diagnosis']

        # 피쳐 임포턴스로 컷오프 진행
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(X, y)

        feature_importances = pd.Series(rf.feature_importances_, index=X.columns)
        feature_importances = feature_importances.sort_values(ascending=False)

        print("Feature Importances:")
        print(feature_importances)

        top_n_features = feature_importances.head(top_features).index.tolist()  # Adjust the number of features as needed

        X_top_features = X[top_n_features]

        df_top_features = pd.concat([X_top_features, y], axis=1)

        # 초기 염색체 생성
        past_population = [
            gda.Chromosome(list(df_top_features.columns), df_top_features, cat_names=[], target='Diagnosis',
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
            final_score,precision,recall,f1 = best_individual.final(df_top_features)
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