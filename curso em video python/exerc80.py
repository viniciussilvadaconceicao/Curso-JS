'''crie um programa onde o usúario possa digitar 5 valores numerico e cadastre-os em uma lista,
já na posição correta de inserção (sem o sort()), no final , mostre a lista ordenada na tela.'''
print('=-'*20)
lista = []
for i in range(0, 5):
    n = int(input('digite um numero:'))
    if n not in lista:
     lista.append(n)
lista.sort()
print(f'a lista dos numeros foram {lista}')