import random
import pandas as pd
import gda


# Configuration
config = {
    'algorithm': 'C4.5',
    'max_depth': 3,
    'enableParallelism': False,
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'population_size': 40,
    'generations': 40,
    'visualizing': True
}

min_samples_split = 0
min_impurity_decrease = 0

# Load the dataset from a local CSV file
column_names = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
    'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'Decision'
]
df = pd.read_csv('../data/wine.csv', header=0, names=column_names)

# Convert target column to object type
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
