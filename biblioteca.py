'''1. Funções
2. A utilização de um Algoritmo de Ordenação, ficando a seu critério a escolha
3. Uso de Arquivos (podendo ser leitura ou escrita)
4. Deve considerar possíveis exceções
'''

from time import sleep

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    try:
        with open('livros.txt', 'a') as arquivo:
            arquivo.write(f'{titulo},{autor}\n')
            print('livro foi adicionado no arquivos de livros')
            sleep(3)
            return menu_principal()
    except IOError:
        print("tente novamente, (ENTRADA OU SAÍDA DEU ERRO.)")
        sleep(3)
        return menu_principal()

def bubble_sort(lista):
    len_lista = len(lista)
    for i in range(len_lista):
        for j in range(len_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def remover_livro(titulo):
    try:
        with open('livros.txt', 'r') as arquivo:
            livros = arquivo.readlines()
        with open('livros.txt', 'w') as arquivo:
            for livro in livros:
                if titulo not in livro:
                    arquivo.write(livro)
            print('Livro foi removido da lista.')
            sleep(3)
            return menu_principal()
    except FileNotFoundError:
        print("Erro usado quando o arquivo não é encontrado por favor verefique o arquivo.")
        sleep(3)

def listar_livros():
    try:
        with open('livros.txt', 'r') as arquivo:
            livros = arquivo.readlines()
            livros = [livro.strip().split(',') for livro in livros]
            livros_ordenados = bubble_sort(livros)
            for livro in livros_ordenados:
                print(f'Título: {livro} ')
                sleep(1)
            print('Programa ira retornar ')
            sleep(2)
            return menu_principal()
    except IOError:
        print("Erro ao abrir o arquivo, (ENTRADA OU SAÍDA DEU ERRO.)")
        sleep(3)
        return menu_principal()
    
def menu_principal():
    print('''
        Bem-vindo à biblioteca!
        Para escolher a opção desejada digite o numero correspondente (1, 2, 3 ou 4 )
        obs: somente numeros seram aceitos.
        Escolha uma das opções, sendo elas:
        
        [1] adiciona livro
        [2] remover livro
        [3] listar livros
        [4] sair
        ''')
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            adicionar_livro()
        elif opcao == 2:
            titulo = input("Digite o título do livro a ser removido: ")
            remover_livro(titulo)
        elif opcao == 3:
            listar_livros()
        elif opcao == 4:
            print('''
        Saindo...
        Obrigado por usar a biblioteca!
        criado por: Vinícius Silva da conceição , tchau...
                  ''')
        else:
            print("Opção inválida, escolha uma opção valida de 1 a 4 ")
            sleep(4)
            return menu_principal()
    except ValueError:
        print("digite um número. (POSSIVEL QUE NÃO USOU UM NUMERO...)")
        sleep(3)

menu_principal()