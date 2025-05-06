class Circulo:
    pi = 3.14156
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.pi * self.radio ** 2
    
circulo1 = 2
print (circulo1)

circulo1 = Circulo(2)
circulo2 = Circulo(4)

print (circulo1.area())
print (circulo2.area())

print (circulo1.pi)
print (circulo2.pi)