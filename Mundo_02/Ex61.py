# EXERCICIO 61

pt = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end=' ')
    termo += ra
    cont += 1
print('acabou')