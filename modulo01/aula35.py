cond = "Sim"

#função lower em vez da função capitalize, só tem que alterar a variavel para minuscúla

while cond.capitalize() == "Sim":

    var = int(input("Digite um número qualquer: "))
    print(f"Número qualquer sendo impresso: {var}")

    cond = input("Você deseja Continuar?\nSim\nNão\n")


print("Fora do While!")
