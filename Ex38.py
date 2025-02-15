#EXERCICIO 38

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
if n1 > n2:
   print('O primerio valor é o maior ({})'.format(n1))
elif n1 == n2:
   print('Os dois valores são iguais!')
else:
   print('O segundo valor é o maior ({})'.format(n2))