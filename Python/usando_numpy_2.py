import numpy as np

## cria uma matriz unidimensional

mt = np.array([12,34,26,18,10])
print(mt)
print(type(mt))

##cria a array com um tipo especifico
#cria o array com float de 64 bits

mtfloat = np.array([1,2,3], dtype = np.float64)
print(mtfloat)
print(type(mtfloat))

mtint = np.array([1,2,3], dtype = np.int32)
print(mtint)
print(type(mtint))