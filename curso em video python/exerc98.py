'''faça um programa que tenha uma FUNÇAO chamada
contador(), que receba tres parametros: inicio, fim e passo e realize a contagem
seguindo a regra:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
def contador(inicio, fim, passo):
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f'{i} ',end='')
        print('FIM')
    else:
        for i in range(inicio, fim-1, -passo):
            print(f'{i} ',end='')
        print('FIM')
    print('\n')
contador(1, 10, 1)
contador(10, 0, 2)
print('agora é sua vez de personalizar a contagem!')
inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('passo:'))
contador(inicio, fim, passo)