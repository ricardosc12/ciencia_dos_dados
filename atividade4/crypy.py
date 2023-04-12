import pandas as pd
import numpy as np
import math
import scipy.stats as stats
# -*- coding: utf-8 -*-

bitcomb = pd.read_csv('./dados/tempo_bitcomb.csv', header=None).squeeze(1)

combinar = pd.read_csv('./dados/tempo_combinar.csv', header=None).squeeze(1)


print("\nBITCOMB")
print(bitcomb.describe())

print("\nCOMBINAR")
print(combinar.describe())

data_bitcomb = bitcomb.values
data_combinar = combinar.values

t_stat, p_val = stats.ttest_ind(data_bitcomb, data_combinar)

print("Estatística t:", t_stat)
print("Valor p:", p_val)