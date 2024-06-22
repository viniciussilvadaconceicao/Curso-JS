'''faça um programa que tenha uma FUNÇÃO escreva()
que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
ex: escreva('ola mundo')'''

def escreva(txt):
    len_txt = len(txt)
    print('='*len_txt)
    print(txt)
    print('='*len_txt)

escreva('ola me chamo vinicius!')
escreva('sou aluno de engenharia de software do 2° periodo')
escreva('em busca de conseguir o primeiro emprego na area de programação')
