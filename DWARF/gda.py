import copy
import math
import random
from typing import List
import pandas as pd
import numpy as np
from chefboost import Chefboost as chef

MIN_DIST_BPS = False
RANGE_TOLERANCE = 1.0
POINT_STRIDE = 5

# 유전자 생성
# 파라미터: 특성 이름, 데이터프레임 인덱스, 최대 이산화 수, 고유값 리스트
# 하나의 유전자는 랜덤한 이산화 포인트를 가짐
# 이산화 포인트는 이산화할 특성의 고유값을 기반으로 생성
class Gene:
    def __init__(self, feature_name: str, df_id: int, max_disc: int = 3, uniq_vals=List[float]):
        self.feature = feature_name # 이산화할 특성
        self.disc_num = random.randint(1, min(max_disc, len(uniq_vals)-1))  # 이산화할 숫자 설정
        self.id = df_id
        # 이산화 0이 되는 오류 수정
        if len(uniq_vals) == 1:
            self.disc_num = 1
        # 이산화 포인트 생성
        if self.disc_num > 1:
            if len(uniq_vals) < self.disc_num:
                raise ValueError('Insufficient Unique Values for Discretization - Check Dataset')
            comb_set = self.get_BPs_Comb(bps=uniq_vals, numSplits=self.disc_num)
            self.break_pts = comb_set
            self.bin = None
            self.label = None


    def __repr__(self):
        name = ''
        if self.disc_num == 1:
            name = 'Feature ({0}) {1} is not selected'.format(self.id, self.feature)
        else:
            name = 'Feature ({0}) {1} discretized with {2} classes - break points: {3}'.format(self.id, self.feature, self.disc_num, self.break_pts)
        return name

    # 이산화 포인트 집합 생성
    # 모든 이산화 포인트의 조합을 생성하고 그 중에서 랜덤하게 선택
    def get_BPs_Comb(self, bps: List[float], numSplits: int) -> List[tuple]:
        bounds = []
        size = len(bps)
        if size < (numSplits - 1):
            return None
        elif size == (numSplits - 1):
            return None
        else:
            bps.sort()
            for i in range(0, size - 1):
                bounds.append(((bps[i] + bps[i + 1]) / 2))

        comb_set = random.sample(bounds, (numSplits - 1))
        comb_set = sorted(comb_set)

        return comb_set

# 염색체
# 파라미터: 특성 이름 리스트, 데이터프레임, 범주형 특성 이름 리스트
# 염색체는 유전자 리스트를 의미
# 염색체는 연속형 변수의 개수만큼의 유전자를 가짐
class Chromosome:
    def __init__(self, attr_names: List[str], df: pd.DataFrame, cat_names: List[str],
                 target='Decision', algorithm='C4.5',max_depth=5):
        gene_list = []
        exclude_attr = [target]
        for id, attr in enumerate(attr_names):
            if attr not in cat_names and attr not in exclude_attr:
                this_bps = np.unique(df[attr]).tolist()
                gene_list.append(Gene(feature_name=attr, max_disc=4, df_id=id, uniq_vals=this_bps))
        self.genes = gene_list
        self.objective = -1
        self.df = df
        self.target = target
        self.model = None
        self.attr_names = attr_names
        self.cat_names = cat_names
        self.config = {
            'algorithm': algorithm,
            'enableParallelism': False,
            'max_depth': max_depth,
        }

    def clone(self):
        # 염색체 복제: 유전자 리스트를 deepcopy하여 새 염색체 생성
        clone_chromosome = Chromosome(self.attr_names, self.df, self.cat_names, f'{self.target}')
        clone_chromosome.genes = copy.deepcopy(self.genes)
        return clone_chromosome

    def __repr__(self):
        return 'Chromosome with {0} features - Objective {1}'.format(len(self.genes), self.objective)

    # 유전자 변이
    # 랜덤하게 하나의 유전자를 선택하고 새로운 이산화 포인트로 갱신
    def mutate(self):
        clone_chromosome = self.clone()
        num_mutations = max(1,len(self.genes)//5) # 염색체의 5분의 1 변이
        mutation_indices = random.sample(range(len(self.genes)), num_mutations)

        for target_id in mutation_indices:
            target_gene = clone_chromosome.genes[target_id]
            this_bps = np.unique(clone_chromosome.df[target_gene.feature]).tolist()
            clone_chromosome.genes[target_id] = Gene(feature_name=target_gene.feature, max_disc=4, df_id=target_gene.id,
                                                     uniq_vals=this_bps)

        return clone_chromosome
    # 교차
    # 파라미터 : 다른 염색체. 교차할 비율
    def crossover(self, other: 'Chromosome', update_ratio=0.3):
        # 두 염색체의 유전자를 교차하여 새 염색체 반환
        new_chromosome = self.clone()
        num_update = math.ceil(len(new_chromosome.genes) * update_ratio)
        update_gene_ids = random.sample(range(0, len(new_chromosome.genes)), num_update)


        for gene_id in update_gene_ids:
            if gene_id < len(other.genes):
                new_chromosome.genes[gene_id] = copy.deepcopy(other.genes[gene_id])
            else:
                print(f"Warning: Gene ID {gene_id} not found in other chromosome.")

        print('Crossover done')
        return new_chromosome

    def evaluate(self, df):
        df_disc = discrete_df(df, self)
        self.model = chef.fit(df_disc, self.config, target_label=self.target, name='model_test')

        # 목적함수: 정확도
        accuracy = self.model['evaluation']['train']['Accuracy']
        self.objective = accuracy

        # 목적함수: F1 Score
        # f1_score = self.model['evaluation']['train']['F1 Score']
        # self.objective = f1_score

        return self.objective
    def final(self, df):
        df_disc = discrete_df(df, self)
        self.model = chef.fit(df_disc, self.config, target_label=self.target, name='model_test')
        accuracy = self.model['evaluation']['train']['Accuracy']
        self.objective = accuracy
        return self.model
# 이산화 데이터프레임 생성
# 파라미터 : 데이터프레임, 염색체
def discrete_df(df: pd.DataFrame, chromo: Chromosome):
    df_copy = copy.deepcopy(df)
    for gene in chromo.genes: # 유전자에 대해 수행 (각 유전자는 연속형 특성을 이산화한 포인트를 의미함)
        if gene.disc_num == 1: # 이산화할 포인트가 없는 경우 해당 특성을 제거
            df_copy = df_copy.drop(columns=[gene.feature])
            continue
        bin = [float('-inf')] # 이산화할 구간 설정
        label = [] # 이산화 레이블 (이름)

        # 이산화 포인트를 기준으로 이산화 구간 설정
        for i in range(len(gene.break_pts)):
            bin.append(gene.break_pts[i])
            label.append('Less_{0}'.format(gene.break_pts[i])) # 브레이크 포인트보다는 작다. 로 표현
        bin.append(float('inf')) # 마지막에 무한대를 추가하여 (-무한 , 브레이크 포인트, 무한)으로 만듦
        label.append('Greater_{0}'.format(gene.break_pts[i])) # 마지막 구간을 이 브레이크 포인트보다는 크다로 표현
        gene.bin = bin # 유전자ㅔ 이산화 구간 설정
        gene.label = label # 레이블 설정
        df_copy[gene.feature] = pd.cut(df_copy[gene.feature], bins=bin, labels=label) # 만들어진 구간으로 레이블로 바꿈 (이산화)
        df_copy[gene.feature] = df_copy[gene.feature].astype('object') # 타입을 오브젝트로 설정
    return df_copy