#variavel global pode ser requisito para alteracao de comportamento de estruturas
from time import sleep

c = 0 
while c < 10 : 
    sleep(1)

    print("\n")

    print(c,'...')

    c = c+1
