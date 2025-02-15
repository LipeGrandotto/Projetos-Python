# EXERCICIO 81

contador = 0
valores = []
while True:
    valor = (int(input('Digite um valor: ')))
    contador += 1
    valores.append(valor)
    p = input('Quer continuar? [S/N]')
    if p in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {contador} valores! ')
print(f'Os valores adicionados em ordem decrescente foram {valores}')
if 5 in valores:
    print('O valor 5 está na lista! ')
else:
    print('O valor 5 não está na lista! ')