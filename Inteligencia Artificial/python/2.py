distacia_pulgadas = [50.5,20.5,20.6,21.05,45.25,100.5]
print(distacia_pulgadas)

#cargamos la libreria
import numpy as np
np_distacia_pulgadas = np.array(distacia_pulgadas)
print(np_distacia_pulgadas)

# operaciones con los array
np_distacia_pulgadas = np_distacia_pulgadas * 0.025
print(np_distacia_pulgadas)

#arreglos con ceros
matriz_ceros = np.zeros(5)
print (matriz_ceros)
#unos
matriz_unos = np.ones(5)
print (matriz_unos)
#rango
matriz = np.arange(0,30+1,2)
print(matriz)

lista1 =[1,2,3]
lista2 =[4,5,6]
lista3 =[7,8,9]
tupla = (lista1, lista2, lista3)
matriz = np.array(tupla)
print (matriz)

print(matriz.shape)
matriz.dtype

print (matriz)
print ('promedio', matriz.mean())
operacion_resta = matriz - matriz.mean()
print (operacion_resta)

#hacer una copia
print(matriz)
copia_matriz = matriz
copia_matriz[copia_matriz<=5] =0
print(copia_matriz)
copia_matriz[0]= 1
print(copia_matriz)
copia_matriz[:,[0] ] = 2
print (copia_matriz)

#random
matriz_aleatoria = np.random.randint(5, 20)
print(matriz_aleatoria)

matriz1 = np.arange(1,1+5)
print(matriz1)
matriz2 = np.arange(5,5+5)
print (matriz2)
suma = matriz1 + matriz2
print (suma)
print(np.max(matriz1))
valor_maximo = np.max(np.maximum(matriz1, matriz2))
print (valor_maximo)

# Resolver un sistema de Ecuaciones
"""
      X2 + X3 = 5
  X1          = 1
           X3 = 3
"""
import numpy as np
A = np.array([[0,1,1],[1,0,0],[0,0,1]])
print(A)
B = np.array([[5],[1],[3]])
print(B)
# calculamos la matriz inversa
inversa = np.linalg.inv(A)
print(inversa)

X = inversa.dot(B)
print('X  es \n',X)