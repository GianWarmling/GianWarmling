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
    "Nacionalidade": nacionalidade,
    "Idioma": idioma
}

print(pessoa)