nome = input ("Digite seu Nome: ")
sobrenome = input ("Digite seu Sobrenome: ")
idade = input ("Digita sua Idade: ")

#Aqui estamos utilizando uma derivação da interpolação de string
#chamada mascara de substituição pois as variaveis vão dentro da função 
print("O nome digitado foi: {} \nO sobrenome é: {} \nA idade é: {}".format(nome, sobrenome, idade))