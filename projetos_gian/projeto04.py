cont = 0
n = int(input("Digite um Valor: "))
if n > 1:
    for i in range(1, 11):
        if n % i == 0:
            cont += 1
        if cont > 2:
            print(f"Não é primo, ele é divisivel {cont} vezes!")
        else:
            print(f"É primo, ele é divisivel apenas {cont} vezes!")
else:
    print("Não é primo!")
    