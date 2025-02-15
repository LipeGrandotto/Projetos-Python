# EXERCICIO 51

print('='*26)
print('    10 TERMOS DE UM PA')
print('='*26)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10 - 1) * r
for c in range (t, decimo + r, r):
   print('{} '.format(c), end='-> ')
print('ACABOU!')