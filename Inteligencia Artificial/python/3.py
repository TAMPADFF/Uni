# comentario
saludo1 = "Hola"
saludo2 = 'Mundo'
print(saludo1, ' esta es una comilla dobel " ', saludo2)

print(saludo1[0])

print(saludo1.upper())

potecias = 5**3
modulo = 105%10
division_entera = 5//5

suma = True

suma = 1 + 2.5
print(suma)

suma = "tres punto cinco"
print(suma)

precio = int(input('ingrese un valor '))

iva = precio*0.12
print ('el iva es ', iva, " Quetzales")
print ("de un total de ", precio, 'Quetzales')

#Condicionales
edad = int(input('ingrese su edad '))

if edad < 18:
  print ('es menor de edad')
  print ('"segunda linea"\n')
elif edad >= 60:
  print ("es adulto mayor")
else:
  print ('mayor de edad')

  #Ciclos
numero = 0
while numero < 4:
  numero = numero + 1
  print(numero)

numero = 'uno'
numero = 0
while True:
  numero = numero + 1
  print (numero)
  if numero >= 4:
    break
  
numero = 'cien'
for letra in numero:
  print (letra)

print(numero[0])

for numero in range(2,10,3):
  print(numero)

  #Listas

lista = 1
listaVacia = []
lista = [1,1.5,'a','hola']
print(lista)    

lista = ['H','o','l','a']
print (lista[0:4:2])

#insertar
lista.insert(2,'l')
print(lista)

for item in lista:
  print(item)   

  #ordenar
lista_desordenada = [1,5,5,8,7,64,4]
print(lista_desordenada)
lista_ordenada = sorted(lista_desordenada)
print(lista_ordenada)

#insertar
lista_vacia = []
print(lista_vacia)
lista_vacia.append(1)
print(lista_vacia)
lista_vacia.append(5)
print(lista_vacia)

lista_vacia.extend([1,2,3])
print(lista_vacia)

#eliminar
del lista_vacia[0]
print(lista_vacia)

captura = lista_vacia.pop(0)
print('se elimino el valor ', captura, ' y queda ahora ', lista_vacia)

#modificar
lista_vacia[0] = 99
print (lista_vacia)


#buscar
buscado = lista_vacia.index(3)
print('el elemento buscado esta en la posicion ', buscado)


#Matriz lista de listas

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print (matriz)
for fila in matriz:
  print(fila)

  #cantidad de filas
print('filas : ',len(matriz))
print('columnas: ',len(matriz[0]))
print(matriz[3-1][3-1]) 

tupla = (1,2,3)
print(tupla)
print(tupla[-1])

tupla = (1,2,3)+(4,5)
print(tupla)

print(tupla)
aux_lista = list(tupla)
aux_lista[0] = 33
tupla = tuple(aux_lista)
print(tupla)

tupla = ((1,2),(3,4))
print(tupla)
print(tupla[0][0])

diccionario_ingles = {"amarillo":'yellow', "rojo":'red', "azul":'blue'}
estudiantes = {"nombre":"pedro", "carnet":'012-2022'}

print(diccionario_ingles["amarillo"])
print(estudiantes["nombre"])

#insert, update
dato = {"blanco":'guait'}
diccionario_ingles.update(dato)
print(diccionario_ingles)
diccionario_ingles.update({"blanco":'white'})
print(diccionario_ingles)

blanco = diccionario_ingles.pop("blanco")
print(blanco)
print(diccionario_ingles)