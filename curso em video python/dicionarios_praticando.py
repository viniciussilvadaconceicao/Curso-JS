estado = dict()
brasil = list()

for i in range(0,3):

    estado['UF'] = str(input('unidade federativa:'))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estado.copy())
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()