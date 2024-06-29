import os 
from time import sleep

'''aqui criei essa função para limpar as telas quando for alternando'''
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

'''aqui criei essa função para retornar ao menu principal quando for chamado'''
def main():
    limpar_tela()
    print('escolha entre 1 e 4 para continuar')
   
    if __name__ == "__main__":
        main()

'''aqui criei essa função para ser uma das telas quando for chamado no caso as informações sobre os identificadores'''
def identificadores():
    limpar_tela()  
    print('='*100)
    print(''' 
        Escolha uma das opções abaixo:
          
        [1]- OQUE PODE FAZER
        [2]- OQUE NÃO PODE FAZER
        [3]- RETORNAR
          ''')
    print('='*100)
    rsp = int(input('Digite a opção desejada: '))
    try:
        if rsp == 1:
            print('''
                IDENTIFICADORES PERMITIDOS:
                  
            - Podem começar com letras, $ ou _
            - Podem conter letras, números, $ e _
            - podem contar com letras acentuadas e símbolos
            ''')

            rsp = int(input('para retornar ao menu principal digite o NUMERO 3:'))
            if rsp == 3:
                return identificadores()
            else:
                print('Opção inválida, tente novamente!')
                sleep(3)
                return identificadores()
            
        elif rsp == 2:
            print('''
                IDENTIFICADORES NÃO PERMITIDOS:
                  
            - Não podem começar com números
            - Não podem conter espaços
            - Não podem conter caracteres especiais
            ''')
            rsp = int(input('Para retornar ao menu principal digite o NUMERO 3:'))
            if rsp == 3:
                return javascript()
            else:
                print('Opção inválida, DIGITE 3 PARA RETORNAR ,tente novamente!')
                sleep(2)
                identificadores()

        elif rsp == 3:
            print('Retornando ao menu principal...')
            return javascript()
        
        else:
            print('Opção inválida, tente novamente!')
            sleep(2)
            identificadores()

    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA ENTRE 1 E 3 PARA CONTINUAR
              ''')
        sleep(2)
        identificadores()

'''aqui criei essa função para ser outra tela no caso as dicas de programação em javascript'''
def dicas():
    limpar_tela()
    print('='*100)
    print('''
        DICAS DE PROGRAMAÇÃO EM JAVASCRIPT:
          
(MAIÚSCULAS E MINUSCULAS) fazem diferenças
tente escolher (NOMES COERENTES) para as variáveis

typeof consegue ver o tipo de primitivo 

number(infinity, NaN)
string
boolean
null
undefined
object(array vetor)
function
          ''')
    print('='*100)
    rsp = int(input('Para retornar ao menu principal DIGITE O NUMERO 3: '))
    try:
        if rsp == 3:
            return javascript()
        else:
            print('Opção inválida, tente novamente!')
            sleep(2)
            return dicas()
        
    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA NUMERO 3 PARA RETORNAR AO MENU PRINCIPAL
              ''')
        sleep(2)
        return dicas()

'''aqui criei essa função para ser mais uma tela de informação no caso a soma em javascript'''
def soma():
    print('='*100)
    print('''
        SOMA EM JAVASCRIPT:
          
number.parseInt (para numeros inteiros 1)
number.parseFloat (para numeros flutoantes ex 1.5)
number (para somar numeros inteiros e flutoantes) 
          ''') 
    print('='*100)
    rsp = int(input('Para retornar ao menu principal DIGITE O NUMERO 3: '))
    try:
        if rsp == 3:
            print('Retornando ao menu principal...')
            return javascript()
        else:
            print('Opção inválida, tente novamente!')
            sleep(2)
            return soma()
        
    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA NUMERO 3 PARA RETORNAR AO MENU PRINCIPAL
              ''')
        sleep(3)
        return soma()   

'''aqui criei essa função para ser o menu principal do programa'''   
def javascript():
    limpar_tela()  
    print('\n')
    print('='*100)
    print('''Esse programa foi criado por Vinicius silva da conceição, com a intenção de ajudar a entender como funciona 
as regras da linguagem JavaScript:
escolha uma das opçções abaixo:

          [1]- IDENTIFICADORES
          [2]- DICAS DE PROGRAMAÇÃO
          [3]- SOMA EM JAVASCRIPT
          [4]- SAIR DO PROGRAMA
          ''')
    print('='*100)
    try:
        rsp = int(input('Digite a opção desejada: '))
        if rsp == 1:
            identificadores()
        elif rsp == 2:
            dicas()
        elif rsp == 3:
            soma()
        elif rsp == 4:
            print('''
        Obrigado por usar o programa, se gostou siga nossa pagina clicando no link logo abaixo:
                  
                      https://github.com/viniciussilvadaconceicao
                   
        Assim que clicar no link ira aparecer Follow link, clique nele para seguir a pagina
                  ,''')
            return
        else:
            print('Opção inválida, tente novamente!')
            sleep(2)
            javascript()
    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA ENTRE 1 E 4 PARA CONTINUAR
              ''')
        sleep(2)
        return
javascript()