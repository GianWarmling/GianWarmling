#Estrutura de Descisão

chopp = int(input("Escreva quantos choppes você tomou: "))

if chopp < 5 : 
    print("Você tomou menos que 5 choppes!")
    print("Se mantenha consciente, pode arrumar problemas com a Lei!")

if chopp == 5 : 
    print("Você tomou 5  choppes!")
    print("Se cuide , pode acabar arrumando problemas com a Lei!")

elif chopp > 5 :
    print("Você tomou mais que 5 choppes, está muito faceiro!")

    multa = float(chopp * 100)
    print("Você irá pagar uma multa de R$ {:.2f}".format(multa))

else:
    print("Erro!!!")