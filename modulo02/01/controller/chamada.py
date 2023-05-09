from model.nome import chamanome
from model.sobrenome import chamasobrenome
from model.idade import chamaidade

def chamamenu():
    nome = chamanome()
    sobrenome = chamasobrenome()
    idade = chamaidade()
    
    print(nome, sobrenome, idade)