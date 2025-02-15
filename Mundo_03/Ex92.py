# EXERCICIO 92

from time import sleep
from datetime import date
atual = date.today().year
dic = {}
dic ['Nome'] = str(input('Nome: '))
dic ['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
idade = atual - dic['Ano de Nascimento'] 
dic ['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dic['Carteira de Trabalho'] != 0:
    dic ['Ano de contratação'] = int(input('Ano de contratação: '))
    aposentadoria = idade + ((dic['Ano de contratação'] + 35) - atual)
    dic ['Salario'] = float(input('Salário: R$ '))
    print('-=' * 28)
    sleep(1)
print(f'Nome tem o valor {dic["Nome"]}.')
print(f'Idade tem o valor {idade}.')
if dic['Carteira de Trabalho'] != 0:
    print(f'CTPS tem o valor {dic["Carteira de Trabalho"]}')
    print(f'O ano de contratação foi {dic["Ano de contratação"]}')
    print(f'Valor do Salário {dic["Salario"]}')
    print(f'A sua aposentadoria será com {aposentadoria} anos.')