'''faça um programa que tenha uma lista chamada números e duas funçoes chamadas sorteia() e soma par()
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
 e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
num = list()

def sorteia():
    from random import randint
    for i in range(0, 5):
        num.append(randint(0, 10))
    print(f'Os valores sorteados pela função são {num}')


def soma_par():
    soma = 0
    cont = 0
    for c in num:
        if c % 2 == 0:
            cont += 1
            soma += c
    print(f'existe {cont} valores , a soma desses valores pares sorteados pela função é {soma}')

sorteia()
soma_par()