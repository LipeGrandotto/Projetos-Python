# EXERCICIO 63

print('-'*35)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*35)
fib = int(input('Quantos termos você quer que mostre? '))
cont = 3
p1 = 0
p2 = 1
print('{} - {}'.format(p1,p2), end= ' ')
while cont <= fib:
    p3 = p1 + p2
    print('- {} '.format(p3), end='')
    cont += 1
    p1 = p2
    p2 = p3
print('\nEsses são os {} primeiro termos de Fibonacci.'.format(fib))