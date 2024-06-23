'''faça um programa que tenha uma função chamada maior(),
que receba vários PARAMETROS com valores inteiros 
seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(valores):
    print('='* 70)
    print('analisando os valores passados...')
    print(f'{valores} foram informados {len(valores)} valores ao todo.')
    print(f'o maior valor informado foi {max(valores)}')
  

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior(valores)
valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
maior(valores)
valores = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
maior(valores)
valores = [20, 5 , 10, 15, 6, 7, 8, 9, 10, 11]
maior(valores)
valores = [0]
maior(valores)
print()