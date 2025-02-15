# EXERCICIO 82

valores = []
impar = []
par = []
while True:
    valor = (int(input('Digite um valor: ')))
    p = str(input('Quer continuar?  [S/N]'))
    if p in 'Nn':
        break
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('=' * 28)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')