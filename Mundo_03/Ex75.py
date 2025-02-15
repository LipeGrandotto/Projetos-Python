# EXERCICIO 75

numeros = (int(input(f'Digite o 1º número: ')),
            int(input(f'Digite o 2º número: ')),
            int(input(f'Digite o 3º número: ')),
            int(input(f'Digite o 4º número: ')))
print(f'Você digitou os valor {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valor pares digitados foram ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')