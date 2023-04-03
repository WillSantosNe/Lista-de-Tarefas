"""
Este programa é um gerenciador de arquivos que permite visualizar, modificar e
excluir arquivos de um diretório. As opções disponíveis são:


Para utilizar o programa, execute o arquivo 'main.py'. É necessário ter o 
Python instalado na sua máquina.


Funções:

def menu() -> int:
    Retorna a opção selecionada pelo usuário.

def menu_opcao2() -> int:
    Retorna a opção selecionada pelo usuário na segunda etapa do menu.

def ver_arquivos(diretorio: str) -> None:
    Exibe todos os arquivos de um diretório.

def input_para_diretorio() -> str:
    Pede ao usuário para inserir o caminho do diretório a ser manipulado.

def diretorio_nao_encontrado() -> str:
    Pede ao usuário para tentar novamente quando um diretório não é encontrado

def verificacao_diretorio(funcao: Callable) -> None:
    Verifica se um diretório existe e executa uma função para ele.

def renomear_arquivo(diretorio: str) -> None:
    Permite ao usuário renomear um arquivo dentro de um diretório específico.

def mover_arquivos(diretorio: str) -> None:
    Permite ao usuário mover um arquivo dentro de um diretório específico.

def copiar_arquivos(diretorio: str) -> None:
    Permite ao usuário copiar um arquivo dentro de um diretório específico.

def remover_arquivos(diretorio: str) -> None:
    Permite ao usuário remover um arquivo dentro de um diretório específico.

def system_clear() -> None:
    Limpa a tela do terminal.

    
O programa utiliza a biblioteca padrão do Python e não requer a instalação de 
pacotes adicionais.

Autor: William Dalla Stella dos Santos
Data: 02/04/2023

Obs: Ainda estou aprendendo, pretendo otimizar cada vez mais esse projeto =)
"""


from funcoes import *
from time import sleep


while True:
    try:
        escolha_usuario = menu()
        if escolha_usuario == 3:
            break

        elif escolha_usuario == 1:
            # Concluido
            verificacao_diretorio(ver_arquivos)
        elif escolha_usuario == 2:
            while True:
                opcao = menu_opcao2()
                if opcao == 5:
                    break
                if opcao == 1:
                    verificacao_diretorio(renomear_arquivo)
                if opcao == 2:
                    verificacao_diretorio(mover_arquivos)
                if opcao == 3:
                    verificacao_diretorio(copiar_arquivos)
                if opcao == 4:
                    verificacao_diretorio(remover_arquivos)
        else:
            print("A opção deve ser [1] [2] ou [3].")
            sleep(2)
    except:
        pass
