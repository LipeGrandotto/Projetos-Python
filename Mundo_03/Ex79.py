# EXERCICIO 79

valores = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso! ')
    else:
        print('Valor duplicado, não será adicionado')
    p = input('Quer continuar? [S/N]')
    if p in 'Nn':
        break
valores.sort()
print(f'Os valores adicionados foram {valores}')