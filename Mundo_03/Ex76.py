# EXERCICIO 76

print('-' * 56)
print('{:^56}'.format('LISTAGEM DE PREÇOS'))
print('-' * 56)

produtos = ('Lápis', 1.75,
        'Borracha', 2.00, 
        'Caderno', 15.90, 
        'Estojo', 25.00, 
        'Transferidor', 4.20, 
        'Compasso', 9.99, 
        'Mochila', 120.32, 
        'Canetas', 22.30, 
        'Livro', 34.90)

for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<42}', end='')
    else:
        print(f'R$ {produtos[pos]:>8.2f}')
print('=' * 56)