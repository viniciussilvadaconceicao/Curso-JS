'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
print('=-'*20)
contador = soma = menor = maior = 0
while True:
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
media = soma / contador
print(f'A média dos valores digitados é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
print('=-'*20)