#EXERCICIO 34

s = float(input('Insira o seu salário: '))
if s <= 1250:
   print('O seu salário é de {} e o aumento de 15% será igual á {}'.format(s,(s*0.15)))
   print('Portanto o seu salário será de {:.2f}'.format((s*0.15)+s))
else:
   print('O seu salário é de {} e o será de 10% será igual á {}'.format(s,(s*0.10)))
   print('Portanto o seu salário será de {:.2f}'.format((s*0.10)+s))