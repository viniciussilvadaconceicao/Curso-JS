'''faça um programa que tenha uma FUNÇÃO chamada áriea(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno'''
def area(lar, comp):
    a =  lar * comp
    print(f'a área de um terreno {lar} por {comp} é de {a} m²')

a = float(input('largura do terreno:'))
b = float(input('comprimento do terreno:'))
area(a, b)
