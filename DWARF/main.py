import dwarf

config = {
    # 디시전 트리 설정
    'algorithm': 'ID3',
    'max_depth': 3,
    'enableParallelism': False,
    # 유전 알고리즘 파라미터 설정 (교차 확률 + 변이 확률+ 생존 확률 = 1)
    'crossover_rate': 0.8,
    'mutation_rate': 0.3,
    'survival_rate': 0.1,

    'population_size': 10,
    'generations': 10,

    'visualizing': True,
    'elitism': 2,
    # 데이터셋 설정
    'top_features': 5,
    'data_name': 'wdbc',
    'train_ratio': 0.7

}

dwarf.dwarfTree(config)

