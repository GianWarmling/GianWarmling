#funcoes com parametros

def soma (a, b, c):
    d = a + b + c
    return d

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

n4 = soma(n1, n2, n3)

print(f"O resultado da soma é: {n4}")
