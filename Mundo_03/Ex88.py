# EXERCICIOS 88

# MINHA SOLUÇÃO

from random import sample

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

print('-' * 35)
print('{:^35}'.format('JOGAR NA MEGA SENA'))
print('-' * 35)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' *4, f'SORTEANDO {quant} JOGOS', '-=' *4)
tamanho = 6
valores = range(1, 61)
for c in range(0, quant):
    print(f'Jogo {c + 1}:  {sample(lista, tamanho)}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5 )

# SOLUÇÃO DO GUANABARA

# from random import randint
# from time import sleep

# lista = []
# jogos = []
# print('-' * 35)
# print('{:^35}'.format('JOGAR NA MEGA SENA'))
# print('-' * 35)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' *4, f'SORTEANDO {quant} JOGOS', '-=' *4)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i + 1}:  {l}')
#     sleep(1)
# print('-=' * 5, '< BOA SORTE! >', '-=' * 5 )