#  EXERCICIO 93

dic = {}
lista = []
dic ['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantos partidas {dic["Nome"]} jogou? '))
for c in range (0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dic ['Gols'] = lista
dic ['Total'] = sum(lista)
print('-=' * 28)
print(dic)
print('-=' * 28)
print(f'O campo nome tem o valor {dic["Nome"]}')
print(f'O campo gols tem o valor {dic["Gols"]}')
print(f'O campo total tem o valor {dic["Total"]}')
print('-=' * 28)
print(f'O jogador {dic["Nome"]} jogou {partidas} partidas.')
for c in range (0, partidas):
    print(f'=> Na partida {c}, fez {(lista[c])} gols')
print(f'Foi um total de {dic["Total"]} gols.')
