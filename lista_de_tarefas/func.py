# Funções usadas para o gerenciamento da lista de tarefas
from os import system, name
from datetime import date

def system_clear():
   """
   Limpa a tela do console de acordo com o sistema operacional 
   em que o programa está sendo executado.
   """
   system('cls' if name == 'nt' else 'clear')

def linhas(n):
    print("-"*n)

def mensagem_menu():
    """
    Aguarda o usuário digitar uma tecla para retornar ao menu principal.
    """
    input("Digite qualque tecla para voltar ao menu principal")


def adicionar_elementos(lista):
    """
    Permite adicionar elementos à lista.

    Parâmetros:
    lista (dict): um dicionário que armazena elementos, seus prazos e momento 
    de adição.

    Returns: None

    A função solicita o nome do elemento, o prazo para entrega e o momento 
    atual de adição. A função irá gerar uma chave para o elemento adicionado 
    e armazená-lo no dicionário lista.

    A função apresentará um menu de opções para o usuário após cada adição de 
    elemento, permitindo que ele continue adicionando elementos ou saia da 
    função.
    """

    contador = 1

    while True:
        system_clear()
        elemento = input("Nome elemento: ")
        para_quando = input("Deve ser entregue em: ")
        momento_adicao = date.today()

        chave_elemento = "elemento"+str(contador)
        contador += 1

        lista[chave_elemento] = {"elemento":elemento, "prazo": para_quando, "momento_adicao":momento_adicao}

        linhas(30)
        resp_usuario = input("Deseja inserir novo elemento? [S/N]")
        if resp_usuario in ["S", 's', 'sim', 'SIM']:
            pass
        else:
            break


def ver_lista(lista):
    """
    Exibe na tela os elementos presentes na lista, incluindo o prazo e a data
    de adição de cada elemento.

    Parâmetros:
        lista: Um dicionário que contém informações sobre cada elemento da lista.

    Returns:None
    """
     
    system_clear()
    
    if len(lista) == 0:
        print("Sem elementos por enquanto")
    else:
        for x, y in lista.items():
            print("Elemento: ", y["elemento"])
            print("Prazo: ", y["prazo"])
            print("Adicionado em: ", y["momento_adicao"])
            linhas(30)




def editar_lista(lista):
   """
    Função que permite editar um elemento da lista.

    Parâmetros:
        lista: um dicionário representando a lista de tarefas a ser editada.

    Returns: None.

    Permite ao usuário editar um elemento existente em uma lista de tarefas. 
    Ela solicita o nome do elemento a ser editado e, em seguida, permite ao usuário
    alterar o nome do elemento, a data de entrega e a data de adição. Se o elemento 
    não estiver na lista, o usuário tem a opção de tentar novamente ou voltar ao 
    menu principal.
    """

   system_clear()
   
   if len(lista.items()) == 0:
       print("Sua lista não possui elementos")
       mensagem_menu()
       return

   elemento_troca = input("Qual elemento será editado (nome): ")
   linhas(30)
   
   for x, y in lista.items():
      if y["elemento"] == elemento_troca:
        elemento = input("Nome elemento: ")
        para_quando = input("Deve ser entregue em: ")
        momento_adicao = date.today()

        lista[x] = {"elemento":elemento, "prazo": para_quando, "momento_adicao":momento_adicao}
        return
   else:
        print("Esse elemento não está na lista.")
        escolha_usuario = input("Deseja tentar novamente?[S/N]")
        if escolha_usuario in ["S", 's', 'sim', 'SIM']:
            editar_lista(lista)



def excluir_elementos(lista):
    """
    Exclui elementos de uma lista.

    Parâmetros:
    lista (dict): um dicionário contendo os elementos a serem excluídos.

    Returns: None.

    Esta função solicita ao usuário que informe o nome do elemento a ser 
    excluído da lista. 
    Caso o elemento seja encontrado, o usuário é questionado se tem certeza
    que deseja excluí-lo e, em caso afirmativo, o elemento é removido da lista.
    Se o elemento não for encontrado, o usuário pode tentar novamente ou 
    voltar para o menu principal.
    """
    
    system_clear()

    if len(lista.items()) == 0:
        print("Sua lista não possui elementos")
        mensagem_menu()
        return

    elemento_excluir = input("Qual elemento será excluído? (nome):")
    linhas(30)

    for x, y in lista.items():
        if y["elemento"] == elemento_excluir:
            escolha_usuario = input("Tem certeza que quer excluir esse elemento? [S/N]")
            if escolha_usuario in ["S", 's', 'sim', 'SIM']:
                lista.pop(x)
                system_clear()
                print("Elemento excluído com sucesso!")
                mensagem_menu()
                return          
    else:
        print("Esse elemento não está na lista.")
        escolha_usuario = input("Deseja tentar novamente?[S/N]")
        if escolha_usuario in ["S", "s"]:
            excluir_elementos(lista)

    


def menu():
    """
    Função que exibe um menu para o usuário e retorna a opção escolhida.

    Retorna:
    - Um inteiro correspondente à opção escolhida pelo usuário.

    Exceções:
    - ValueError: caso a opção digitada pelo usuário não seja um número.

    """

    while True:
        system_clear()
        print("----------MENU DA LISTA----------")
        print("[1] Ver a lista")
        print("[2] Modificar lista")
        print("[3] Fechar programa")
        print("")
        try:
            _resp_usuario = int(input("Opção: "))
            return _resp_usuario
        except ValueError:
            print("ERRO: A opcao deve ser um número!!!")



           