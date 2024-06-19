'''crie um programa que vai ler varios números e colocar em uma lista 
depois disso, mostre:
a) quantos números foram digitados
b) a lista de valores ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista'''
print('=-'*20)
list = []
contador = 0
while True:
    n = int(input('digite um numero:'))
    contador += 1
    if n not in list:
        list.append(n)

    resposta = str(input('quer continuar ? [S/N] sendo S para sim e N para não:')).strip().upper()
    if resposta == 'N':
        break
list.sort(reverse=True)
print(f'''
foram lidos {contador} elementos 
sua lista de forma decrescente é {list}''') 
if 5 in list:
    print('o valor 5 foi digitado e está na lista')
else:
    print('o valor 5 não foi digitado e não está na lista')
print('\n')
print('=-'*20)