from time import sleep

situacao = "Reprovado"

situacao == "Reprovado"

### bloco 1
nome = input("Digite o Seu Nome: ")
sobre_nome = input("Digite seu Sobrenome: ")
idade = int(input("Digite Sua Idade: "))

###bloco 2
nota1 = float(input("Digite Sua Primeira Nota: "))

nota2 = float(input("Digite Sua Segunda Nota: "))

media = (nota1 + nota2) / 2
print(media)

###bloco 3
if media < 7:

    situacao = "Reprovado"
    print(f"Infelizmente você REPROVOU!\nSua Média foi: {media}")

elif media >= 7:
    for c in range(0, 10):
        print("*")
        sleep(1)
    situacao = "Aprovado"
print("Parabéns você foi APROVADO!\nSua Média foi: {}".format(media))

dicionario ={
    "Nome": nome,
    "Sobrenome": sobre_nome,
    "Idade": idade,
    "Nota1": nota1,
    "Nota2": nota2,
    "Média": media,
    "Situação": situacao
}

print(f'''{dicionario['Nome']}\n{dicionario['Sobrenome']}\n{dicionario['Idade']}\n{dicionario['Nota1']}\n{dicionario['Nota2']}\n{dicionario['Média']}\n{dicionario['Situação']}''')
