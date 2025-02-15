# EXERCICIO 90

dic = {}
dic ['nome'] = str(input('Nome: '))
dic ['media'] = float(input(f'Média do {dic["nome"]}: '))
print(f'Nome é igual a {dic["nome"]} ')
print(f'Média é igual a {dic["media"]} ')
if dic['media'] > 6:
    print('Situação é igual a APROVADO.')
else:
    print('Situação é igual a REPROVADO.')