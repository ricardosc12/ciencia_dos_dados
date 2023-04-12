import pandas as pd
import numpy as np
import math
import scipy.stats as stats
# -*- coding: utf-8 -*-

ie666 = pd.read_csv('./dados/atraso_ie666.csv', header=None).squeeze(1)

ia171 = pd.read_csv('./dados/atraso_ia171.csv', header=None).squeeze(1)


print("\nIE666")
print(ie666.describe())

print("\nIA171")
print(ia171.describe())

data_ie666 = ie666.values
data_ia171 = ia171.values

t_stat, p_val = stats.ttest_ind(data_ie666, data_ia171)

print("Estatística t:", t_stat)
print("Valor p:", p_val)