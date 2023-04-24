# Importação Otimizada
from random import choice

nome1 = input("Digite seu Nome: ")
nome2 = input("Digite seu Nome: ")
nome3 = input("Digite seu Nome: ")
nome4 = input("Digite seu Nome: ")

#Variavel recebendo uma lista definida pela simbologia [],
lista = [   nome1,
            nome2,
            nome3,
            nome4
            ]

sorteado = choice(lista)

#print utilizando polimorfismo e quebra de linhas
print("="*20, "NOME SORTEADO", "="*20)

if sorteado == nome1 :
    print("O nome sorteado foi o primeiro digitado")
    print(f"O nome sorteado foi {sorteado}")

elif sorteado == nome2 :
    print("O nome sorteado foi o segundo digitado")
    print(f"O nome sorteado foi {sorteado}")

elif sorteado == nome3 :
    print("O nome sorteado foi o terceiro digitado")
    print(f"O nome sorteado foi {sorteado}")

elif sorteado == nome4 :
    print("O nome sorteado foi o quarto digitado")
    print(f"O nome sorteado foi {sorteado}")

else : 
    print("ERRO")