from func import *

lista = {

}

while True:
    opcao_menu = menu()
    if opcao_menu == 3:
        break
    elif opcao_menu == 2:
        system_clear()
        print("----------MODIFICAR LISTA----------")
        print("[1] Adicionar elementos")
        print("[2] Editar elementos")
        print("[3] Excluir elementos")
        print("[4] Voltar ao menu principal")
        try:
            resp_usuario = int(input("Opção: "))
        except ValueError:
            print("ERRO: A opcao deve ser um número!!!")

        if resp_usuario == 4:
            menu()
        elif resp_usuario == 1:
            adicionar_elementos(lista)
        elif resp_usuario == 2:
            editar_lista(lista)
        elif resp_usuario == 3:
            excluir_elementos(lista)
        else:
            print("Escolha uma opção válida!")
            input("Pressione qualque tecla para tentar novamente")
    elif opcao_menu == 1:
        ver_lista(lista)
        input("Pressione qualquer tecla para voltar ao menu")
