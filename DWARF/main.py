# import random
# import pandas as pd
# import gda
#
#
# # 설정 -> 알고리즘을 좀 바꾸자
# config = {
#     'algorithm': '초',
#     'max_depth': 3,
#     'enableParallelism': False,
#     'crossover_rate': 0.8,
#     'mutation_rate': 0.3,
#     'population_size': 10,
#     'generations': 1,
#     'visualizing': True
# }
#
# min_samples_split = 0
# min_impurity_decrease = 0
#
# DROP_FEATURES = ['Material(Family)', 'Serial num', 'Cause P/No Desc.', '유형별', '귀책별', 'Region Name', 'Vendor Name',
#                  'Material(Class)', 'Operation Hour']
#
#
# def main():
#     df = pd.read_excel('dataset/DIV_Sample_Data.xlsx')
#     df = df.drop(columns=DROP_FEATURES)
#     df = df.astype(float)
#     df['Decision'] = df['Decision'].astype('object')
#
#     initial_population = [
#         gda.Chromosome(list(df.columns), df, cat_names=[], target='Decision', min_samples_split=min_samples_split,
#                        min_impurity_decrease=min_impurity_decrease) for _ in range(config['population_size'])]
#
#     def is_duplicate(new_chromosome, population):
#         for chromo in population:
#             if new_chromosome.genes == chromo.genes:
#                 return True
#         return False
#
#     for generation in range(config['generations']):
#         print(f"Generation {generation + 1}")
#         unique_initial_population = []
#         for individual in initial_population:
#             if not is_duplicate(individual, unique_initial_population):
#                 unique_initial_population.append(individual)
#         initial_population = unique_initial_population
#
#         evaluated_population = [(individual, individual.evaluate(df)) for individual in initial_population]
#         evaluated_population.sort(key=lambda x: x[1], reverse=True)
#
#         best_individual, best_score = evaluated_population[0]
#         print(f"Best Individual in Generation {generation + 1}: {best_individual}")
#         print(f"Best Score: {best_score}")
#
#         new_population = []
#         for _ in range(config['population_size']):
#             parent1 = random.choice(evaluated_population)[0]
#             parent2 = random.choice(evaluated_population)[0]
#             if random.random() < config['crossover_rate']:
#                 offspring = parent1.crossover(parent2)
#             else:
#                 offspring = parent1.clone()
#             if random.random() < config['mutation_rate']:
#                 offspring = offspring.mutate()
#             new_population.append(offspring)
#
#         unique_new_population = []
#         for individual in new_population:
#             if not is_duplicate(individual, unique_new_population):
#                 unique_new_population.append(individual)
#         initial_population = unique_new_population
#
#     best_individual, best_score = evaluated_population[0]
#     final_score = best_individual.evaluate(df)
#
#     print(f"Final Evaluation Score: {final_score}")
#
#
# if __name__ == "__main__":
#     main()


# Using UCI dataset
import random
import pandas as pd
import gda
import pydotplus
from sklearn.datasets import load_wine
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from IPython.display import Image

# 설정
config = {
    'algorithm': '초',
    'max_depth': 3,
    'enableParallelism': False,
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'population_size': 100,
    'generations': 100,
    'visualizing': True
}

min_samples_split = 0
min_impurity_decrease = 0

def main():
    # Load the wine dataset
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['Decision'] = wine.target

    df = df.astype(float)
    df['Decision'] = df['Decision'].astype('object')

    initial_population = [
        gda.Chromosome(list(df.columns), df, cat_names=[], target='Decision', min_samples_split=min_samples_split,
                       min_impurity_decrease=min_impurity_decrease) for _ in range(config['population_size'])]

    def is_duplicate(new_chromosome, population):
        for chromo in population:
            if new_chromosome.genes == chromo.genes:
                return True
        return False

    for generation in range(config['generations']):
        print(f"Generation {generation + 1}")
        unique_initial_population = []
        for individual in initial_population:
            if not is_duplicate(individual, unique_initial_population):
                unique_initial_population.append(individual)
        initial_population = unique_initial_population

        evaluated_population = [(individual, individual.evaluate(df)) for individual in initial_population]
        evaluated_population.sort(key=lambda x: x[1], reverse=True)

        best_individual, best_score = evaluated_population[0]
        print(f"Best Individual in Generation {generation + 1}: {best_individual}")
        print(f"Best Score: {best_score}")

        new_population = []
        for _ in range(config['population_size']):
            parent1 = random.choice(evaluated_population)[0]
            parent2 = random.choice(evaluated_population)[0]
            if random.random() < config['crossover_rate']:
                offspring = parent1.crossover(parent2)
            else:
                offspring = parent1.clone()
            if random.random() < config['mutation_rate']:
                offspring = offspring.mutate()
            new_population.append(offspring)

        unique_new_population = []
        for individual in new_population:
            if not is_duplicate(individual, unique_new_population):
                unique_new_population.append(individual)
        initial_population = unique_new_population

    best_individual, best_score = evaluated_population[0]
    final_score = best_individual.evaluate(df)

    print(f"Final Evaluation Score: {final_score}")


if __name__ == "__main__":
    main()