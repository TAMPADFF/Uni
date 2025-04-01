import numpy as np

# Arreglos A y B con 10 números definidos por mí
A = np.array([15, 22, 38, 45, 10, 56, 78, 64, 23, 89])
B = np.array([15, 22, 38, 46, 10, 56, 78, 64, 23, 89])

# Mostrar los arreglos
print("Arreglo A:", A)
print("Arreglo B:", B)

# Verificar si los arreglos son iguales
if np.array_equal(A, B):
    print("Los arreglos son iguales.")
else:
    print("Los arreglos son diferentes.")

