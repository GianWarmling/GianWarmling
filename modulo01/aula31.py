#importacao otimizada por conta do from
#modulo time
#funcao sleep
from time import sleep 

inicio = int(input("Digite o número de inicio: "))
fim = int(input("Digite o número de fim: "))
passo = int(input("Digite o número de passo: "))

for cronometro in range(inicio, fim, -passo) :
    sleep(3)
    print(cronometro)
