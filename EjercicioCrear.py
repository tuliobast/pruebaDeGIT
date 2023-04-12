import pickle

class Vehiculo:
    marca = None
    modelo = None
    puertas = 4
    velocidad = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        self.velocidad += 10 
        return self.velocidad
    
    def frenar(self):
        self.velocidad -+ 10
        return self.velocidad

auto = Vehiculo('Ford', 'Fiesta')
auto.acelerar()
auto.acelerar()
auto.acelerar()
f = open('carro.bin', 'wb')
pickle.dump(auto, f)
f.close()

f = open('carro.bin', 'rb')
autoGuardado = pickle.load(f)
f.close()

print(autoGuardado.marca)
print(autoGuardado.velocidad)