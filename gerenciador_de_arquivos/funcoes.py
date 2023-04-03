import os

def linhas(n):
    print("-"*n)


def input_para_diretorio():
    """
    Solicita ao usuário que insira o caminho para 
    uma pasta e retorna o caminho inserido.

     Retorna:
        str: O caminho completo para o diretório informado pelo usuário.

    """
    linhas(60)
    diretorio = input("Entre com o caminho da pasta: ")
    return diretorio


def diretorio_nao_encontrado():
    """
    Exibe mensagem de erro informando que o diretório não foi encontrado 
    e solicita ao usuário que decida se deseja tentar novamente.

    Retorna:
        str: Resposta do usuário, indicando se deseja ou não tentar novamente.
        Opções válidas: "S" ou "N".
    """
    while True:
        system_clear()
        print("ERRO. Diretorio nao encontrado!")
        escolha_usuario = input("Deseja tentar novamente? [S/N]")
        return escolha_usuario


def verificacao_diretorio(funcao):
    """
    Função que verifica se o diretório informado pelo usuário é válido e 
    chama a função 'funcao' com o diretório como argumento. Se o diretório
    não existir, o usuário tem a opção de tentar novamente ou voltar ao menu
    principal.

    Parâmetros:
        função : funcao
            Função que será chamada com o diretório como argumento.

    Retorna: None
    """
    while True:
        diretorio = input_para_diretorio()
        if os.path.isdir(diretorio):
            funcao(diretorio)
            linhas(60)
            input("Digite qualquer valor para retornar ao menu")
            break
        else:
            escolha_usuario = diretorio_nao_encontrado()
            if escolha_usuario in ["SIM","S","sim","s", 'Sim']:
                continue
            else:
                break


def system_clear():
    """
    Limpa a tela do terminal usando o comando de acordo com o 
    sistema operacional.

    Retorna: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """
    Apresenta o menu de opções do programa Gerenciador de Arquivos.
    Retorna a opção escolhida pelo usuário.

    Retorna:
        int: Inteiro representando a opção escolhida pelo usuário.
    """
    system_clear()
    print('--------MENU GERENCIADOR DE ARQUIVOS--------')
    print("[1] Visualizar arquivos")
    print("[2] Modificar arquivos")
    print("[3] Sair do Programa")

    return int(input("Opcao: "))


def menu_opcao2():
    """
    Imprime as opções do menu de modificação de arquivos e retorna a opção 
    escolhida pelo usuário.

    Retorna:
        int: Inteiro representando a opção escolhida pelo usuário.
    """
    system_clear()
    print("--------MODIFICAR ARQUIVOS--------")
    print("[1] Renomear arquivo")
    print("[2] Mover arquivo")
    print("[3] Copiar arquivo")
    print("[4] Excluir arquivo")
    print("[5] Voltar ao menu principal")
    return int(input("Opcao: "))


def renomear_arquivo(diretorio):
    """
    Renomeia um arquivo no diretório especificado nos parâmetros.
    Caso o arquivo não seja encontrado o usuário tem opção de tentar
    novamente ou voltar para o menu de modificação.

    Args:
        diretorio: str
            O caminho do diretório em que o arquivo se encontra.

    Retorna: None.
    """
    system_clear()
    print("Arquivos disponíveis neste diretório:")
    ver_arquivos(diretorio)

    print("----------------RENOMEAR ARQUIVO----------------")
    nome_arquivo = input("Nome atual do arquivo: ")

    if nome_arquivo in os.listdir(diretorio):
        novo_nome = input("Novo nome para o arquivo: ")
        os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome))
        
        linhas(60)
        print("Arquivo renomeado com sucesso!")
    else:
        linhas(60)
        print("Arquivo não encontrado")
        escolha_usuario = input("Deseja tentar novamente? [S/N]")
        if escolha_usuario in ["SIM","S","sim","s"]:
            renomear_arquivo(diretorio)
        else:
            return


def copiar_arquivos(diretorio):
    """
    Copia um arquivo de um diretório para outro.

    Pede para o usuário digitar o nome do arquivo que deseja copiar. 
    Em seguida, pede o caminho até o diretório de destino. Se o arquivo já 
    existir no diretório de destino, é criado outro com uma extensão numérica 
    após o nome.

    Args:
        diretorio: str 
            Caminho para o diretório de origem.

    Retorna: None.
    """
    from shutil import copy2
    from pathlib import Path

    # Mostrando os arquivos disponíveis para copiar
    system_clear()
    print("Arquivos disponíveis neste diretório:")
    ver_arquivos(diretorio)

    # Pegando o caminho até o arquivo
    print("----------------COPIAR ARQUIVO----------------")
    nome_arquivo = input("Nome atual do arquivo: ")
    origem = os.path.join(diretorio, nome_arquivo)

    # Pegando o caminho até o destino
    destino = input("Entre com o caminho para o novo local: ")
    diretorio_destino = Path(destino)
    nome_arquivo = Path(origem).name

    # Verificação caso o arquivo já exista no diretório
    # Em caso afirmativo, será criado outro com uma extensão após o nome
    if diretorio_destino.joinpath(nome_arquivo).exists():
        contador = 1
        while diretorio_destino.joinpath(f"{nome_arquivo}_{contador}").exists():
            contador += 1
        nome_arquivo, extensao_arquivo = os.path.splitext(nome_arquivo)
        novo_nome = f"{nome_arquivo}({contador})" + str(extensao_arquivo)
    else:
        novo_nome = nome_arquivo

    # Copiando arquivo para o diretório destino
    copy2(origem, diretorio_destino.joinpath(novo_nome))


def ver_arquivos(diretorio):
    """
    Lista os arquivos presentes no diretório especificado.

    Args:
        diretorio: str
            Caminho do diretório a ser listado.

    Retorna: None.
    """
    system_clear()
    os.chdir(diretorio)

    for x in os.listdir():
        print(x)
    

def mover_arquivos(diretorio):
    """
    Move um arquivo de um diretório para outro.

    Args:
        diretorio: str 
            Caminho para o diretório do arquivo.

    Retorna: None.
    """
    from shutil import move

    system_clear()
    print("Arquivos disponíveis neste diretório:")
    ver_arquivos(diretorio)
    
    print("----------------MOVER ARQUIVO----------------")
    nome_arquivo = input("Nome do arquivo: ")

    # Verificando se o arquivo está no diretório informado
    if nome_arquivo in os.listdir(diretorio):
        origem = os.path.join(diretorio, nome_arquivo)
        while True:
            destino = input("Entre com o caminho até a pasta destino: ")

            # Verificando se o diretório destino existe
            if os.path.isdir(destino):
                destino = os.path.join(destino, nome_arquivo)

                # Verificando se o diretório de destino é o mesmo da origem
                if destino == origem:
                    system_clear()
                    print("O arquivo não pode ser movido para o mesmo lugar.")
                    return
                break
            else:
                escolha_usuario = diretorio_nao_encontrado()
                if escolha_usuario in ["SIM","S","sim","s", 'Sim']:
                    linhas(60)
                    continue
                else:
                    break
    else:
        system_clear()
        print(f"O arquivo {nome_arquivo} não existe nesse diretório!")
        input("Pressione qualquer tecla para tentar novamente")
        mover_arquivos(diretorio)

    # Realizando a mudança de diretório
    move(origem, destino)
    print("Arquivo movido com sucesso.")


def remover_arquivos(diretorio):
    """
    Remove um arquivo do diretório especificado pelo usuário.

    Args:
        diretorio: str
            O caminho absoluto para o diretório onde se encontra o arquivo a 
            ser removido.
.
    Retorna: None
    """
    system_clear()
    print("Arquivos disponíveis neste diretório:")
    ver_arquivos(diretorio)
    
    print("----------------REMOVER ARQUIVO----------------")
    nome_arquivo = input("Nome do arquivo: ")
    if nome_arquivo in os.listdir(diretorio):
        verificacao = input(f"Tem certeza de deseja remover o arquivo {nome_arquivo}? [S/N]")
        if verificacao in ["SIM","S","sim","s", 'Sim']:
            os.remove(nome_arquivo)
            system_clear()
            print("Elemento removido com sucesso!")
            return

    else:
        system_clear()
        print(f"O arquivo {nome_arquivo} não existe nesse diretório!")

        escolha_usuario = input("Deseja tentar novamente? [S/N]")
        if escolha_usuario in ["SIM","S","sim","s", 'Sim']:
            remover_arquivos(diretorio)
        else:
            return
        

        