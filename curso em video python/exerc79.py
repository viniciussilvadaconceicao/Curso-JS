'''crie um programa onde o usúario possa digitar vários valores numericos e cadrastre-os em uma lista,
caso o numero ja exista la dentro, ele não será adicionado.
 No final, serão exibidos todos os valores unicos digitados em ordem crescente.'''

print('=-'*20)
lista = []
while True:
    n = float(input('digite um valor:'))
    if n not in lista:
        lista.append(n)
    
    resposta = str(input('quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

lista.sort()
print(f'os valores digitados foram: {lista}')

'''primeiro criar uma lista vazia ,
depois criamos um laço de repetição com o while true pois com ele podemos usar o break para sair do laço
lo apos iso criei uma vaiavel para armazenar um valor, e um if caso o numero digitado não estiver na lista ira armazenar usando o .append()
depois criei uma variavel para perguntar se o usuario quer continuar digitando, se a resposta for 'N' o laço se encerra com o break
criando outro if para saber qual foi a resposta do usuario e se for 'N' o laço se encerra com o break
para finalizar usei o .sort() para ordenar a lista em ordem crescente e printei a lista com os valores digitados se eu quisesse em ordem decrescente
usaria o .sort(reverse=True)'''