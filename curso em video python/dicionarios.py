'''para identificar um dicionario, usamos chaves {} e para identificar uma lista, usamos colchetes []
no dicionario, podemos usar chaves para identificar um valor, por exemplo:
pessoa = {'nome':'gustavo', 'idade':22, 'sexo':'M'} não esquecendo que o dicionario é uma coleção de dados que contem chave e valor'''
'''para criar um dicionario vazio, usamos pessoa = {} ou pessoa = dict()'''
dados = dict()
dados = {'nome':'vinicius', 'idade':27}
dados['sexo']='M'
print(dados['nome'])
print(dados)

'''para deletar um item do dicionario, usamos del dados['sexo']'''
del dados['sexo']
print(dados)
print('\n')

filme1 = {'titulo':'star wars',
         'ano':1977,
         'diretor':'george lucas'
         }

filme2 = {'titulo':'avengers',
          'ano': 2012,
          'diretor':'joss whedon'
          }

filme3 = {'titulo':'matrix',
          'ano':1999,
          'diretor':'wachowski'
          }

'''usamos o . values() para mostrar os valores do dicionario,
 o .keys() para mostrar as chaves do dicionario 
 e o .items() para mostrar os itens do dicionario'''

print(filme1.values())
print(filme1.keys())
print(filme1.items())
print('\n')
for k,v in filme1.items():
    print(f'o {k} é {v}')
print('\n')

locadora = list()
locadora.append(filme1)
print(locadora)

