# Se define la clase Circulo
class Circulo:
    # Atributo de clase 'pi', accesible para todos los objetos de la clase
    pi = 3.14156

    # Constructor de la clase: recibe el radio como argumento
    def __init__(self, radio):
        self.radio = radio  # Guarda el radio en un atributo de instancia

    # Método que calcula el área del círculo
    def area(self):
        return Circulo.pi * self.radio ** 2  # Fórmula del área del círculo: pi * radio^2

# Se asigna simplemente el número 2 a la variable circulo1 (no es un objeto todavía)
circulo1 = 2
print(circulo1)  # Imprime el número 2

# Ahora circulo1 se convierte en un objeto de la clase Circulo
circulo1 = Circulo(2)
# Se crea un segundo objeto circulo2 de la clase Circulo
circulo2 = Circulo(4)

# Se llama al método area() para circulo1 y se imprime el resultado
print(circulo1.area())  # Área de un círculo de radio 2

# Se llama al método area() para circulo2 y se imprime el resultado
print(circulo2.area())  # Área de un círculo de radio 4

# Se imprime el valor de pi desde el objeto circulo1
print(circulo1.pi)
# Se imprime el valor de pi desde el objeto circulo2
print(circulo2.pi)


# Definición de una clase llamada Tarjeta
class Tarjeta:

    # Constructor que inicializa el número de la tarjeta y el saldo
    def __init__(self, numero, cantidad=0):
        self.numero = numero  # Número de la tarjeta
        self.saldo = cantidad  # Saldo inicial (por defecto 0)

    # Método especial __str__ para mostrar el objeto como una cadena legible
    def __str__(self):
        return 'Tarjeta numero ' + self.numero + ' Saldo ' + str(self.saldo)

# Se crea un objeto 't' de tipo Tarjeta con número y saldo
t = Tarjeta('01-00025-02', 1000)
print(t)  # Imprime la información de la tarjeta usando el método __str__


# Ahora se redefine (reescribe) la clase Tarjeta
class Tarjeta:

    # Nuevo constructor (parecido al anterior, pero cambia 'numero' a 'id')
    def __init__(self, id, cantidad=0):
        self.id = id
        self.saldo = cantidad

    # Método __str__ para mostrar información de la tarjeta
    def __str__(self):
        return 'Tarjeta numero ' + self.id + ' Saldo ' + str(self.saldo)

    # Método para mostrar explícitamente el saldo
    def mostrar_saldo(self):
        print('El saldo es', self.saldo, 'Q.')

# Se define una nueva clase que hereda de Tarjeta
class Tarjeta_descuento(Tarjeta):

    # Constructor que recibe id, descuento y saldo
    def __init__(self, id, descuento, cantidad=0):
        self.id = id
        self.saldo = cantidad
        self.descuento = descuento  # Porcentaje de descuento

    # Método propio de Tarjeta_descuento para mostrar el descuento
    def mostrar_descuento(self):
        print('Descuento de', self.descuento, '%')

# Se crea un objeto 't' de tipo Tarjeta_descuento
t = Tarjeta_descuento('1-000125-01', 5, 1000)

# Se muestra el saldo usando el método heredado de Tarjeta
t.mostrar_saldo()

# Se muestra el descuento usando el método propio de Tarjeta_descuento
t.mostrar_descuento()


# Se reutiliza la variable 'tarjeta' varias veces cambiando su valor
tarjeta = 'Hola'  # 'tarjeta' ahora es una cadena de texto
print(tarjeta)

tarjeta = 1  # 'tarjeta' ahora es un número entero
print(tarjeta)

tarjeta = Tarjeta('15-1515-01', 1000)  # 'tarjeta' ahora es un objeto Tarjeta
print(tarjeta)

tarjeta = Tarjeta_descuento('15-1515-01', 5, 2000)  # 'tarjeta' ahora es un objeto Tarjeta_descuento
print(tarjeta)

# Se verifica si 'tarjeta' es instancia de Tarjeta
print(isinstance(tarjeta, Tarjeta))  # True, porque Tarjeta_descuento hereda de Tarjeta

# Se verifica si 'tarjeta' es instancia de Circulo
print(isinstance(tarjeta, Circulo))  # False, no tiene relación con Circulo