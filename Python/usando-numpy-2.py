import numpy as np

##Usando matrix unidimensional
mt = np.array([12,13,35,36,40,41])
print(mt)
print(type(mt))

##criar array com um tipo especifico
##cria a array com float de 64bit

mtfloat = np.array([1,2,3], dtype=np.float64)
print(mtfloat)
print(type(mtfloat))

##criar arrau com tipo especifico
##criar a array com inteiro de 32 bits

mtint = np.array([1,2,3,4], dtype=np.int32)
print(mtint)
print(type(mtint))

##mudar o tipo de array
##podendo transformar os tipos de dados do array

mtnew = np.array([1.4,3.6,-5.1,9.42,4.999999])
print(mtnew)

##quando transformar de float para int os valores sao truncados

mtnewint = mtnew.astype(np.int32)
print(mtnewint)

##podendo fazer o inverso tambem
mt5 = mtnewint.astype(float)
print(mt5)

##criando mais de uma dimensao
##matriz bidimencional

mt7 = np.array([[7,2,33],[8,6,9],[10,55,30]])
print(mt7)

##criar arrays vazios tipificados
##empty significa que não sao inicializados, não que sao vazios

vazio = np.empty([3,2], dtype=int)

print('-------')
print(vazio)
print('-------')

##cria matriz  4x3 com valores zeros

zeros = np.zeros([4,3])
print(zeros)
print('-------')

##com valor igual a um

um = np.ones([5,7])
print(um)
print('-------')

##cria matriz quadrada com diagonal principal com valores 1 e outros valores 0

diagonal = np.eye(5)
print(diagonal)
print('-------')

##valores aleatorios entre zero e um

ale = np.random.random((5))
print(ale)
print('-------')

##valores aleatorios com negativos

ale2 = np.random.randn((5))
print(ale2)
print('-------')

##valores aleatorios 3x4

ale3 = (10*np.random.random((3,4)))
print(ale3)
print('-------')

##outras formas de gerar aleatorios

gnr = np.random.default_rng(1)
ale5 = gnr.random(3)
print(ale5)
print('-------')

##gerar inteiros
ale6 = gnr.integers(10, size=(3,4))
print(ale6)
print('-------')

##unique remove as repeticoes

j = np.array([11,11,11,12,13,14,14,15,16,17])
j = np.unique(j)
print(j)
print('-------')