import random
import pandas as pd
import numpy as np
import utils as prep
import gda

def dwarfTree(config):
# 데이터 로드
    X,y= prep.load_data(config['data_name'])
    # 데이터 분할 및 컷오프
    df_train, df_test = prep.cut_off_and_split(X, y, config['top_features'], config['train_ratio'])

    # 초기 염색체 생성
    past_population = [
        gda.Chromosome(list(df_train.columns), df_train, cat_names=[], target='Decision',
                       algorithm=config['algorithm']) for _ in range(config['population_size'])]

    # 생존 염색체, 변이 염색체, 교차 염색체 수 설정
    mutation_size = int(config['population_size'] * config['mutation_rate'])
    crossover_size = int(config['population_size'] * config['crossover_rate'])
    survival_size = int(config['population_size'])-mutation_size-crossover_size

    # 유전 알고리즘 수행
    for generation in range(config['generations']):
        print(f"Generation {generation + 1}")

        new_population = past_population

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

        # 평가 후 정렬
        evaluated_population = [(individual, individual.evaluate(df_train)) for individual in new_population]
        evaluated_population.sort(key=lambda x: x[1], reverse=True)
        # 생존 염색체 선정
        past_population = [individual for individual, _ in evaluated_population[:survival_size]]
        best_individual, best_score = evaluated_population[0]
        print(f"Generation {generation} Score: {best_score}")

# 결과 출력
    best_individual, best_score = evaluated_population[0]
    final_score,precision,recall,f1 = best_individual.final(df_test,f"{config['data_name']}_{config['algorithm']}_{best_score}",config)

