print("Seja muito bem vindo as quiz do Gian!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n(A)Rockstar Games \n(B) Ubisoft \n(C) Activision \n(D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
    print("Sua pontuação é: ", score)
else:
    print("Incorreto!")
    print("Sua pontuação é: ", score)

print("Qual o nome do protagonista do jogo GTA San Andreas?\n(A) Carlos John\n(B) Carl Jonhson\n(C) Carl Jaqueline\n(D) Carlos Jonhson")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
    print("Sua pontuação é: ", score)
else:
    print("Incorreto!")
    print("Sua pontuação é: ", score)

print(f"Sua pontuação final é: {score}/2")