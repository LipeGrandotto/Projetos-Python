# EXERCICIO 46

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
   print(c)
print('FIM')

s = 0
for c in range (0, 4):
   n = int(input('Digite um valor: '))
   s += n
print('O somatório de todos os valores foi {}'.format(s))

#EXERCICIO 46.2

from time import sleep
for c in range (10, -1, -1):
   print(c)
   sleep(1)
print('BUM! BUM! POOOW!')
