import pandas as pd
import numpy as np
import math
# -*- coding: utf-8 -*-

# series = pd.Series(np.random.randint(-1000,1000,size=500),dtype=int)

# max = series.max()
# min = series.min()

# positive_values = series.loc[lambda x: x>=0]

# impares_values = series.loc[lambda x: x%2!=0]

# between = series.iloc[50:101]

# par_values = len(series.loc[lambda x: x%2==0])

# min_500 = len(series.loc[lambda x: x>=500])

# min_500_max_700 = series.loc[lambda x: np.logical_and(x>=500,  x<700)]

# square = series.apply(lambda x: math.sqrt(x) if x>0 else float("NaN"))

# print(square)]

# escola = {
#     "JK":{
#         "turmas":{
#             "comp":{
#                 "alunos":[
#                     {"nome":"Ricardo", "nota":5},
#                     {"nome":"Mari", "nota":5}
#                 ]
#             }
#         }
#     }
# }
def generateAluno(x):
    turma = turmas[np.random.randint(0,4)]
    disciplina = disciplinas[np.random.randint(0,4)]
    return ("Aluno "+str(x), disciplina, turma, np.random.randint(0,101))


disciplinas = ["compiladores","distribuidos","pdi","meta_heuristica"]
turmas = [1,2,3,4]
alunos = np.array(list(map(lambda x: tuple(generateAluno(x)), np.random.randint(0,30,size=10))))

# (aluno, disciplina, turma, nota)
alunos = pd.Series(alunos.tolist())

df = pd.DataFrame(alunos.tolist(), columns=['Aluno', 'Disciplina', "Turma", "Nota"])
print(df)

print("Turma 4")
notas = alunos.apply(lambda x: [x[0],x[3]] if int(x[2])==4 else None).dropna()
df_notas = pd.DataFrame(notas.tolist(), columns=["Aluno","Nota"])
print(df_notas)

print("Média notas turma 4")
mean = notas.apply(lambda x: x[1]).median()
print(mean)

print("Alunos de compiladores")
comp = alunos.apply(lambda x: [x[0],x[3]] if x[1]=="compiladores" else None).dropna()
df_comp = pd.DataFrame(comp.tolist(), columns=["Aluno","Nota"])
print(df_comp)

print("\n\nAlunos por disciplina")
print(df.groupby("Disciplina")["Aluno"].count())

print("\n\nMédia das notas dos estudantes")
print(df.groupby("Aluno")["Nota"].median())
