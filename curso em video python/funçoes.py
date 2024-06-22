def mostralinha():
    print('-='*30)

mostralinha()
print('SISTEMA DE ALUNOS')
mostralinha()
print()

def mensagem(txt):
    print('-='*30)
    print(txt)
    print('-='*30)

mensagem('ola me chamo vinicius!')

def soma(a,b):
    s = a + b
    print(s)
 

soma(20, 1)
soma(5, 6)
soma(1990, 7)
print('-='*30)
print('\n')

def contador(*núm):
    tam = len(núm)
    print(f'recebi os valores {núm} , que tem {tam} elementos')
    for i in núm:
        print(f'{i} ',end='')
    print('FIM')
    print('\n')


contador(1, 2, 3, 4, 5)
contador(6, 7, 8, 9)
contador(10, 11)

'''para conta quantos elementos tem em uma tupla ou lista, 
basta usar o len() e passar a lista ou tupla como parametro'''
def dobra(valores):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(f'os valores dobrado são, {valores}')
