
# EXERCICIO 84.2

# MINHA RESOLUÇÃO 

listanome = []
listapeso = []
tot = 0

while True:
    listanome.append(str(input('Digite seu nome: ')))
    listapeso.append(float(input('Digite seu peso: ')))
    resp = str(input('Quer continuar? [S/N]'))
    tot += 1
    if resp in 'Nn':
        break
listafinal = list(zip(listanome, listapeso))
listafinal.sort(key=lambda x: x[1])
print(f'Tiveram {tot} pessoas cadastradas! ')
print(f'As pessoas mais pesadas foram {listafinal[-1],listafinal[-2]}!')
print(f'As pessoas mais leves foram {listafinal[0], listafinal[1]}!')

# RESOLUÇÃO DO GUANABARA

# temp = []
# princ = []
# mai = men = 0
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp [1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp [1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Quer continuar? [S/N]'))
#     if resp in 'Nn':
#          break
# print('-=' * 28)
# print(f'Tiveram {len(princ)} pessoas cadastradas!')
# print(f'O maior peso foi de {mai}kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'{p[0]}', end=' ')
# print(f'\nO menor peso foi de {men}kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'{p[0]}', end='')
# print()