# EXERCICIO 60

from math import factorial
n = int(input('Digite um número para calculcar seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calculcar seu Fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
   print('{}'.format(c), end=' ')
   print(' x ' if c > 1 else ' = ', end=' ')
   f *= c
   c -= 1
print('{}'. format(f))