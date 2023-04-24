#Sorteio: apenas um resultado(aleatório)
from random import shuffle, choice

import random
n1 = str(input("Digite um Nome: "))
n2 = str(input("Digite um Nome: "))
n3 = str(input("Digite um Nome: "))
n4 = str(input("Digite um Nome: "))

#Array

lista = [ n1, n2, n3, n4]
print(lista)
sorteio = choice(lista)

print(sorteio)
