import random
import pandas as pd
import numpy as np
import utils as prep
import gda
import time
def dwarfTree(config):
    # # 데이터 로드
    # X,y= prep.load_data(config['data_name'])
    # # 데이터 분할 및 컷오프
    # df_train, df_test = prep.cut_off_and_split(X, y, config['top_features'], config['train_ratio'])
    # 데이터 로드
    name = config['data_name']
    df_train = pd.read_csv(f'../data/{name}/train_test_split/{name}_train.csv', header=None)

    # 첫 번째 행을 컬럼으로 지정하고 데이터 타입 변환
    df_train.columns = df_train.iloc[0]
    df_train = df_train.drop(df_train.index[0])

    # 타겟 컬럼 지정
    target_col = 'Decision'

    # 데이터 타입 변환
    df_train[df_train.columns.difference([target_col])] = df_train[df_train.columns.difference([target_col])].apply(
        pd.to_numeric, errors='coerce')

    # 결측치 제거
    df_train = df_train.dropna()

    print(df_train.head())

    # 테스트 데이터에 대해서도 동일하게 처리
    df_test = pd.read_csv(f'../data/{name}/train_test_split/{name}_test.csv', header=None)
    df_test.columns = df_test.iloc[0]
    df_test = df_test.drop(df_test.index[0])

    df_test[df_test.columns.difference([target_col])] = df_test[df_test.columns.difference([target_col])].apply(
        pd.to_numeric, errors='coerce')
    df_test = df_test.dropna()

    print(df_test.head())
    # 초기 염색체 생성
    past_population = [
        gda.Chromosome(list(df_train.columns), df_train, cat_names=[], target='Decision',
                       algorithm=config['algorithm']) for _ in range(config['population_size'])]

    # 생존 염색체, 변이 염색체, 교차 염색체 수 설정
    mutation_size = int(config['population_size'] * config['mutation_rate'])
    crossover_size = int(config['population_size'] * config['crossover_rate'])
    survival_size = int(config['population_size'] * config['survival_rate'])
    random_size = config['population_size'] - mutation_size - crossover_size - survival_size



    # 세대별 결과를 저장할 리스트 초기화
    generation_results = []

    # 유전 알고리즘 수행
    for generation in range(config['generations']):
        print(f"Generation {generation + 1}")
        start_time = time.time()  # 시작 시간 측정

        new_population = past_population.copy()

        # 변이 염색체 생성
        for _ in range(mutation_size):
            parent = random.choice(past_population)
            offspring = parent.mutate()
            new_population.append(offspring)

        # 교차 염색체 생성
        for _ in range(crossover_size):
            parent1 = random.choice(past_population)
            parent2 = random.choice(past_population)
            offspring = parent1.crossover(parent2)
            new_population.append(offspring)
        # 랜덤 염색체 생성
        for _ in range(random_size):
            new_population.append(
                gda.Chromosome(list(df_train.columns), df_train, cat_names=[], target='Decision',
                               algorithm=config['algorithm']))
        # 평가 후 정렬
        evaluated_population = []
        for individual in new_population:
            accuracy, precision, recall, f1_score = individual.evaluate(df_train)
            evaluated_population.append((individual, accuracy, precision, recall, f1_score))

        evaluated_population.sort(key=lambda x: x[1], reverse=True)  # 정확도를 기준으로 정렬

        # 생존 염색체 선정
        past_population = [individual for individual, _, _, _, _ in evaluated_population[:survival_size]]
        best_individual, best_accuracy, best_precision, best_recall, best_f1 = evaluated_population[0]
        end_time = time.time()  # 종료 시간 측정
        elapsed_time = end_time - start_time  # 소요 시간 계산

        print(f"Generation {generation + 1} - Best Accuracy: {best_accuracy}")

        # 결과 저장
        generation_results.append({
            'Generation': generation + 1,
            'Accuracy': best_accuracy,
            'Precision': best_precision,
            'Recall': best_recall,
            'F1 Score': best_f1,
            'Elapsed Time': elapsed_time
        })

    # 결과 출력
    best_individual, best_accuracy, best_precision, best_recall, best_f1 = evaluated_population[0]
    final_score, precision, recall, f1 = best_individual.final(
        df_test,
        f"{config['data_name']}_{config['algorithm']}_{best_accuracy}",
        config
    )

    # 결과를 데이터프레임으로 변환하여 CSV 파일로 저장
    results_df = pd.DataFrame(generation_results)
    results_df.to_csv(f'./log/{config["data_name"]}_{config["algorithm"]}_generation_results.csv', index=False)
    print("Generation results saved to CSV file.")

