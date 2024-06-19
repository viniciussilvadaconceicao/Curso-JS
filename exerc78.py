'''faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
no final mostre qual o maior e o menor valor digitado e as suas respectivas posições na lista'''
print('=-'*20)
lista = []
maior = menor = 0
for i in range(0, 5):
    n = float(input('digite um numero: '))
    lista.append(n)
    if i == 0:
        maior = menor  = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'''
      os numeros digitados foram: {lista},
     o maior numero digitado foi {maior} , e o menor numero digigitado foi {menor}
''')
print('=-'*20)

