n1 = int(input("Digite um Número: "))

resultado = n1 % 2

print("O Resultado é {}".format(resultado))

if resultado == 0 :
    print("O número é par")

#Poderia usar else em vez do ELIF:
elif resultado ==1 :
    print("O número é ímpar")
