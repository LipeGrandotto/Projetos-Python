# EXERCICIO 73

print('=' * 56)
print('{:^56}'.format('TABELA DO BRASILEIRÃO'))
print('=' * 56)

brasileirao = ('Botafogo','Palmeiras','Internacional','Fortaleza','Flamengo','São Paulo','Cruzeiro','Bahia','Corinthians','Atlético-MG','Vasco','Vitória','Juventude','Athelico Paranaense','Grêmio','Fluminense','Criciúma','Bragantino','Cuiabá','Atlético-GO')
print('=' * 56)
print(f'Listas de times do Brasileirão: {brasileirao}')
print('=' * 56)
print(f'Os 5 primeiros colocados do brasileirão são {brasileirao[0:5]}')
print('=' * 56)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('=' * 56)
print(f'Times em ordem alfabética:{sorted(brasileirao)}')
print('=' * 56)
print(f'O Flamengo está na {brasileirao.index("Flamengo")+1}ª posição')