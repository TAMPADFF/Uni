class Tarjeta:

    def __init__(self, numero, cantidad = 0):
        self.numero = numero
        self.saldo = cantidad
        return

    def __str__(self):
        return 'Tarjeta numero '+self.numero + ' Saldo ' + str(self.saldo)

t = Tarjeta('01-00025-02', 1000)
print(t)

