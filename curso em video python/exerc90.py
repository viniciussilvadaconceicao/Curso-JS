'''faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''
aluno = {}
turma = []

aluno['aluno'] = str(input('nome do aluno: '))
aluno['media'] = float(input('digite a media do aluno:'))
turma.append(aluno.copy())

if turma[0]['media'] >= 7:
    turma[0]['situação'] = 'aprovado'
else:
    turma[0]['situação'] = 'reprovado'

print(f'o aluno {turma[0]["aluno"]} com a media {turma[0]["media"]} está {turma[0]["situação"]}')
