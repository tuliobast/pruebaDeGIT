class Vehiculo:
    color = 'white'
    ruedas = 4
    puertas = 5

class Coche:
    coche = Vehiculo()
    velocidad = 100
    cilindrada = 8

carro = Coche()
print(carro.coche.color)
