import pandas as pd
import numpy as np
import math

series = pd.Series(np.random.randint(-1000,1000,size=500),dtype=int)

# max = series.max()
# min = series.min()

# positive_values = series.loc[lambda x: x>=0]

# impares_values = series.loc[lambda x: x%2!=0]

# between = series.iloc[50:101]

# par_values = len(series.loc[lambda x: x%2==0])

# min_500 = len(series.loc[lambda x: x>=500])

# min_500_max_700 = series.loc[lambda x: np.logical_and(x>=500,  x<700)]

# square = series.loc[lambda x: x>=0].apply(lambda x: math.sqrt(x))

# print(square)

alunos = pd.Series([
    {"turma":1,"aluno":"Mari","disci":'comp',"nota":5},
    {"turma":1,"aluno":"Ric","disci":'comp',"nota":5},
    {"turma":1,"aluno":"Mari","disci":'comp',"nota":1},
])
