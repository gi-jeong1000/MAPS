import dwarf
import pandas as pd
# 안되는 데이터셋: Obesity,ionosphere,credit_approval,bank_marketing
for i in ['blood_transfusion','breast_cancer_wisconsin','EyeState','glass', 'heart', 'iris','libras','PageBlocks','parkinsons','PenDigits','pima','satellite','spambase','vertebral_column','waveform','wine']:
    config = {
        # 디시전 트리 설정
        'algorithm': 'ID3',
        'max_depth': 3,
        'enableParallelism': False,

        # 유전 알고리즘 파라미터 설정 (교차 확률 + 변이 확률+ 생존 확률 = 1)
        'crossover_rate': 0.4,
        'mutation_rate': 0.3,
        'random_rate': 0.2,
        'survival_rate': 0.1,

        'population_size': 300,
        'generations': 100,

        # 데이터셋 설정
        'top_features': 5,
        'data_name': 'wine',
        'train_ratio': 0.7

    }

    dwarf.dwarfTree(config)

