from random import choice
n1 = float (input("Digite um número: "))
n2 = float (input("Digite um número: "))
n3 = float (input("Digite um número: "))
n4 = float (input("Digite um número: "))
n5 = float (input("Digite um número: "))

lista = [n1, n2, n3, n4, n5]

sorteio = choice(lista)

if sorteio == n1 :
    for c in range(20):
        print("*")
    print("O número sorteado foi: ", n1)

elif sorteio == n2 :
    for c in range(20):
        print("*")
    print("O número sorteado foi: ", n2)

elif sorteio == n3 :
    for c in range(20):
        print("*")
    print("O número sorteado foi: ", n3)

elif sorteio == n4 :
    for c in range(20):
        print("*")
    print("O número sorteado foi: ", n4)

elif sorteio == n5 :
    for c in range(20):
        print("*")
    print("O número sorteado foi: ", n5)
