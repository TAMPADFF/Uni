class HolaMundo:
    pass
print(HolaMundo)

cadena = 'python'
print(cadena.upper())

class HolaMundo:
    mensaje = 'Hola mundo'

    def __init__(self, nombre):
        self.nombre = nombre
        return

    def mensajeHola(self):
        print(self.mensaje," -- ",self.nombre)
        return

hola = HolaMundo('Marcos')
hola.mensajeHola()