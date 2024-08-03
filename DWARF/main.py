import random
import pandas as pd
import gda
from sklearn.ensemble import RandomForestClassifier

# config 파일 설정
config = {
    'algorithm': 'C4.5',
    'max_depth': 5,
    'enableParallelism': False,
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'population_size': 20,
    'generations': 20,
    'visualizing': True,
    'elitism': 2
}

top_features = 7

def main():
    # 데이터 로드
    column_names = [
        'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'Decision'
    ]
    df = pd.read_csv('../data/wine.csv', header=0, names=column_names)
    df['Decision'] = df['Decision'].astype('object')

    X = df.drop(columns=['Decision'])
    y = df['Decision']

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
        final_score = best_individual.evaluate(df_top_features)
        print(f"Generation {generation} Score: {final_score}")

        # Elitism 적용
        past_population = [individual for individual, _ in evaluated_population[:config['elitism']]]


if __name__ == "__main__":
    main()