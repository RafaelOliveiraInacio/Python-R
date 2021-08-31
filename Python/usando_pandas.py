import pandas as pd

##carrega arquivo pra data frame pandas

dados = pd.read_csv("Credit.csv")

##formato

print(dados.shape)

##resumo estatostocp de cpçimas mi,erocas
print(dados.describe())

##primeiros registros

print(dados.head)

##ultimos registros, com parametros

print(dados.tail(2))

##filtrar por nome da coluna

print(dados[["duration"]])

dados.rename(columns={'duration':'duracao'}, inplace=True)

print(dados[['duracao']])