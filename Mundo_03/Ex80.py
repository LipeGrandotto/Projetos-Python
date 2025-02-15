# EXERCICIO 80

import bisect
lista = []
for i in range(5):
    n = int(input('Digite um valor: '))
    bisect.insort(lista, n)
    print(f'O valor {n} foi colocado na posição {lista.index(n)}')
print(f'Os valores digitados em ordem foram {lista}')

# VARIAÇÃO GUANABARA 

# lista = []
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print(f'Número ao final da lista...')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 print(f'Adicionado na posição {pos} da lista...')
#                 break
#             pos += 1
# print('-=' * 28)
# print(f'Os valores digitados em ordem foram {lista}')