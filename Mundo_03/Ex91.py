# EXERCICIO 91

from random import randint 
from time import sleep
from operator import itemgetter
dic = {'Jogador 01': randint(1,6),
        'Jogador 02': randint(1,6),
        'Jogador 03': randint(1,6),
        'Jogador 04': randint(1,6)}
ranking = []
print('-' * 38)
print('{:^38}'. format('Valores sorteados: '))
print('-' * 38)
for k, v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-' * 38)
print('{:^38}'.format('RANKING DOS JOGADORES'))
print('-' * 38)
ranking = sorted(dic.items(), key = itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'{i} lugar: {v[0]} com {v[1]}')
    sleep(1)
