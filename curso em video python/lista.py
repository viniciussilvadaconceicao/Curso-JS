'''em lista pode usar os comandos
 .append('') para adicionar um elemento na lista
.insert(0, '') para adicionar um elemento na posição 0
del lista[0] para deletar um elemento na posição 0
.pop(0) para deletar um elemento na posição 0
.remove('') para deletar um elemento pelo valor'''

valores = [8,2,5,4,9,3,6]
'''para ordenar a lista'''
valores.sort()
'''para adicionar um elemento na lista , sempre no final'''
valores.append(0)
'''para ordenar a lista de forma reversa'''
valores.sort(reverse=True)
print(valores)
'''para saber o tamanho da lista'''
len(valores)
print(f'Essa lista tem {len(valores)} elementos')