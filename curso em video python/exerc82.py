''' crie um programa que vai ler vários números e colocar em uma lista,
depois disso , crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
ao final, mostre o conteudo das tres listas geradas.'''
lista = []
pares = []
impares = []
while True:
    n = int(input('digite um numero:'))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    resposta = str(input('quer continuar [S/N] sendo S para sim e N para não:')).strip().upper()
    if resposta == 'N':
         break
    
lista.sort()
pares.sort()
impares.sort()
print(f'''
      lista de numeros digitados: {lista}

      lista de numeros pares: {pares}

      lista de numeros impares: {impares}
''')