# EXERCICIO 69

cont = 0
contM = 0
contF18 = 0
while True:
    print('-=' *25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-=' *25)
    if sexo == 'M':
        contM += 1
    if sexo == 'F' and idade <= 20:
        contF18 += 1
    if idade >= 18:
        cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == "N":
        break
print('-=' *25)
print(f'Foram cadastrados {contM} homens, {contF18} mulheres menores de 20 anos e tiveram {cont} pessoas acima de 18 anos.')
print('-=' *25)
print('PROGRAMA ENCERRADO')