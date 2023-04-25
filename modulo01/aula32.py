numero = int(input("Digite um número referente a tabuada que você deseja saber: "))

#tabuada é apenas uma variavel qualquer, poderia ser usado qualquer outra palavra ou letra!

for tabuada in range(0, 11) :
    print("{} X {} = {}".format(numero, tabuada, numero*tabuada))
