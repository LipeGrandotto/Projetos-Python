# EXERCICIO 62

pt = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
            print('{} -> '.format(termo), end=' ')
            termo += ra
            cont += 1
    print('PAUSA')
    mais = int(input('Quantos termo você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('ACABOU!')