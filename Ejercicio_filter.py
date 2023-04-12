from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]
lista1 = filter(lambda x: x % 2, lista)
#print(list(lista1)
lista2 = reduce(lambda a,b: a+b, lista1)
print(lista2)
