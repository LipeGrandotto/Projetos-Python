from Dados.sistema.dado import *
from Dados.arquivo.texto import *
from time import sleep


arq = 'listCadastro.txt'

if not arquivo(arq):
    criararquivo(arq)
while True:
    resposta = cabecalho(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2) 