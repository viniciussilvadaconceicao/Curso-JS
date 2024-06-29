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
           
para adicionar casas decimais use .toFixed(x) para adicionar x casas decimais
          
Para trocar o ponto por virgula use .replace('.', ',') e vice versa EX: 58.5 => 58,5
          
.tolocaleString('pt-BR', {style: 'currency', currency: 'BRL'}) para adicionar o R$ na frente do valor REAL
          
para outras moedas troque o BRL pela sigla da moeda ex: USD, EUR, JPY
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

'''aqui criei essa função para ser mais uma tela de informação no caso formatar strings em javascript'''
def string():
    print('='*100)
    print('''
        FORMATANDO STRINGS EM JAVASCRIPT:
          
          string.toUpperCase() - para transformar uma string em maiuscula
          string.toLowerCase() - para transformar uma string em minuscula
          string.length() - para saber o tamanho da string
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
            return string()
        
    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA NUMERO 3 PARA RETORNAR AO MENU PRINCIPAL
              ''')
        sleep(3)
        return string()

'''aqui criei essa função para ser mais uma tela de informação no caso transformar um numero em string'''
def transformar_numero_string():
    print('='*100)
    print('''
        TRANSFORMAR UM NUMERO EM STRING:
          
          string(number)- para transformar um numero em string
          n.toString() - para transformar um numero em string
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
            return transformar_numero_string()
    except ValueError:
        print('''           
               **********ATENÇÃO**********
            ESCOLHA NUMERO 3 PARA RETORNAR AO MENU PRINCIPAL
              ''')
        sleep(3)
        return transformar_numero_string()
    
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
          [3]- SAIR DO PROGRAMA
          [4]- NUMEROS EM JAVASCRIPT
          [5]- TRANSFORMAR UM NUMERO EM STRING
          [6]- FORMATAR STRINGS EM JAVASCRIPT
          ''')
    print('='*100)
    try:
        rsp = int(input('Digite a opção desejada: '))
        if rsp == 1:
            identificadores()
        elif rsp == 2:
            dicas()
        elif rsp == 3:
            print('''
        Obrigado por usar o programa, se gostou siga nossa pagina clicando no link logo abaixo:
                  
                      https://github.com/viniciussilvadaconceicao
                   
        Assim que clicar no link ira aparecer Follow link, clique nele para seguir a pagina
                  ,''')
            return
        elif rsp == 4:
            limpar_tela()
            soma()

        elif rsp == 5:
            limpar_tela()
            transformar_numero_string()
        
        elif rsp == 6:
            limpar_tela()
            string()

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