##Variaveis de ambiente recebendo valor

delta = 8
print(delta)

##Variaveis de ambiente recebendo valor e printando tipo do objeto recebido.

numero = 8
class(numero)

##Variaveis de ambiente recebendo valor e convertendo para o TIPO INTEIRO (L)

num_int = 8L
class(num_int)

##Variaveis de ambiente recebendo valor logico

logico = T
class(T)

##Variaveis de ambiente recebendo valor condicional 

a = 1
b = 2

condicao = a > b

class(condicao)

print(condicao)

##Trabalhando com vetores

matriz = c(1,2,3,4,5,6,7,8,9,10)

class(matriz)

matriz[1]
matriz[2]
matriz[3]
matriz[4] = 10

#Trabalhando com matriz

VADeaths ##MATRIZ JA PRONTA
colnames(VADeaths)
rownames(VADeaths)

VADeaths[,1]
VADeaths[1,]
VADeaths[1:3,]

##Trabalhando com Data Frame

longley

##Funciona como matriz

longley[,3,1]

##Acessar coluna com $

longley$Unemployed

##Acessar coluna com nome

longley['Unemployed']


##Trabalhando com listagem

ability.cov

##Accessando elementos da listagem

ability.cov$cov

ability.cov[1]

##Verificando objetos diferentes da listagem

class(ability.cov$cov)
class(ability.cov$center)

##Acessando elemento dentro da listagem

ability.cov$cov[,1:3]


##Trabalhando com fatores

state.region

state.region[1]
state.region[1:3]

class(state.region)
