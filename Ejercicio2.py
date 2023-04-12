import pprint

class Alumno:
    nombre = ''
    nota = None

    def setNombre(self, nombre):
      self.nombre = nombre

    def getNombre(self):
      return (f'Mi nombre es, {self.nombre}')
    
    def setNota(self, nota):
      self.nota = nota

    def getNota(self):
      return self.nota
       
    
    def siAprobo(self):
      if self.nota>9:
         print('Estoy aprobado')
      else:
         print('Reprobe')
    
alum1 = Alumno()
alum1.setNombre("alejandra")
alum1.setNota(20)
print(alum1.getNombre())    
print(alum1.getNota())
alum1.siAprobo()    
pprint.pprint(globals())