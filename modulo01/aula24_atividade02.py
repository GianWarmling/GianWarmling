nome = input("Digite seu Nome: ")

cor = input("Informe sua Raça: ")

sexo = input("Digite seu Sexo: ")

tamanho = float(input("Informe sua Altura: "))

peso = float(input("Informe seu Peso: "))

nacionalidade = input("Informe onde você nasceu: ")

idioma = input("Informe seu Idioma principal: ")

pessoa = {
    "Nome": nome,
    "Cor": cor,
    "Sexo": sexo,
    "Tamanho": tamanho,
    "Peso": peso,
    "País": nacionalidade,
    "Idioma": idioma
}

cond = int(input('''Digite o número que representa a características que você deseja saber
\n1_ Nome
\n2_ Cor
\n3_ Sexo
\n4_ Tamanho
\n5_ Peso
\n6_ País
\n7_ Idioma
\n8_ Completo
\n >>>>>>> '''))

if cond == 1:
    print(f" O nome que você deseja saber é: {pessoa['Nome']}")

elif cond == 2:
    print(f" A cor que você deseja saber é: {pessoa['Cor']}")

elif cond == 3:
    print(f" O sexo que você deseja saber é: {pessoa['Sexo']}")

elif cond == 4:
    print(f" A altura que você deseja saber é: {pessoa['Tamanho']}")

elif cond == 5:
    print(f" O peso que você deseja saber é: {pessoa['Peso']}")
    
elif cond == 6:
    print(f" A nacionalidade que você deseja saber é: {pessoa['País']}")

elif cond == 7:
    print(f" O idioma que você deseja saber é: {pessoa['Idioma']}")

elif cond == 8:
    print(pessoa)

