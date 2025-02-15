def jogador (jog='<desconhecido>', gol=0):
    print('-=' * 28)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# PROGRAMA PRINCIPAL
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gol=g)
else:
    jogador(n,g)
