# EXERCICIO 87

soma1 = soma2 = maior = 0
matrizbase = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range(0, 3):
        matrizbase[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 28)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matrizbase[l][c]:^5}]', end='')
        if matrizbase [l][c] % 2 == 0:
            soma1 += matrizbase [l][c]
    print()
print('-=' * 28)
print(f'A soma dos valores pares é {soma1}.')
for l in range(0,3):
    soma2 += matrizbase[l][2]
print(f'A soma dos valores da terceira coluna é {soma2}.')
for c in range(0,3):
    if c == 0:
        maior = matrizbase[1][c]
    elif matrizbase [1][c] > maior:
        maior = matrizbase[1][c]
print(f'O maior valor da segunda linha é {maior}.')