salario1 = float(input("Digite o primeiro salário: "))
salario2 = float(input("Digite o segundo salário: "))
salario3 = float(input("Digite o terceiro salário: "))
salario4 = float(input("Digite o quarto salário: "))


soma = (salario1 + salario2 + salario3 + salario4)

print("="*20," CALCULADORA ", "="*20)

print("O primeiro salário é: {:.2f}\nO segundo salário é: {:.2f}\nO terceiro salário é: {:.2f}\nO quarto salário é: {:.2f}".format(salario1, salario2, salario3, salario4))
print("\n")
print("O resultado da soma é:\n================= {:.2f} =================".format(soma))
