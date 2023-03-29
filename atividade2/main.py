import pandas as pd
import numpy as np
import math
import scipy

series = pd.read_csv('./series.csv', index_col=False, header=None, squeeze=True)
men_height_series = pd.read_csv('./altura_homens.csv', index_col=False, header=None, squeeze=True)
women_height_series = pd.read_csv('./altura_mulheres.csv', index_col=False, header=None, squeeze=True)

print("MIN, MAX")
print("Dados dos homens: ")
print('O valor mínimo é: {}'.format(men_height_series.min()))
print('O valor máximo é: {}'.format(men_height_series.max()))

print("Dados das mulheres: ")
print('O valor mínimo é: {}'.format(women_height_series.min()))
print('O valor máximo é: {}'.format(women_height_series.max()))

print("MEDIA MEDIANA")
print("Dados dos homens: ")
print('O valor media é: {}'.format(men_height_series.mean()))
print('O valor mediana é: {}'.format(men_height_series.median()))

print("Dados das mulheres: ")
print('O valor media é: {}'.format(women_height_series.mean()))
print('O valor mediana é: {}'.format(women_height_series.median()))

print("Desvio Padrão")
print("Dados dos homens: ")
print('O valor desvio padrao é: {}'.format(men_height_series.std()))
# print('O valor mediana é: {}'.format(men_height_series.median()))

print("Dados das mulheres: ")
print('O valor desvio padrao é: {}'.format(women_height_series.std()))

print("Homens menores que 160cm")
print("{} %".format(len(men_height_series.loc[lambda x: x<160])/len(men_height_series)*100))

print("Mulheres maiores que 180cm")
print("{} %".format(len(women_height_series.loc[lambda x: x>180])/len(women_height_series)*100))

print("O percentil de homens com altura menor que 160cm")
print(sum(np.abs(men_height_series) < 160) / float(len(men_height_series))*100)

print("O percentil de mulheres com altura maior que 180cm")
print(sum(np.abs(women_height_series) > 180) / float(len(women_height_series))*100)

print("3 alturas mais frequentes homens")
# print(pd.Series(men_height_series.value_counts().values[:3]).reindex(men_height_series.value_counts().index[:3]))
print(pd.Series(men_height_series.value_counts()).iloc[:3])
print(sum(men_height_series.value_counts().values[:3]))

print("Distancia em desvios padroes da media da mulher")
media = women_height_series.mean()
desvio = women_height_series.std()
altura = 185

print(media)
print(desvio)
print(altura)
print((altura-media)/desvio) #ZSCORE

# print('O valor mediana é: {}'.format(women_height_series.median()))

# print('O valor mínimo é: {}'.format(men_height_series.min()))

# # Máximo
# print('O valor máximo é: {}'.format(men_height_series.max()))

# # Média
# print('O valor da média é: {:.2f}'.format(men_height_series.mean()))

# # Desvio Padrão
# print('O valor do desvio padrão é: {:.2f}'.format(men_height_series.std()))

# # Moda
# print('A moda é: {}'.format(men_height_series.mode()))

# print(sum(np.abs(men_height_series) < 185) / float(len(men_height_series)))
# array_p = np.percentile(men_height_series,50)
# print(array_p)