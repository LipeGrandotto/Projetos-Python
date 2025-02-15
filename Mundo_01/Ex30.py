#EXERCICIO 30

n = int(input('Me diga um número qualquer: '))
result = n % 2
if result == 0:
   print('O número {} é par!'.format(n))
else:
   print('O número {} é ímpar!'.format(n))