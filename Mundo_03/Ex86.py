#  EXERCICIO 86

matrizbase = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range(0, 3):
        matrizbase[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 28)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matrizbase[l][c]:^5}]', end='')
    print()