# EXERCICIO 28

nome = input('Qual é seu nome? ')
if nome == 'Luiz':
   print ('Que nome lindo voê tem! ')
else:
   print('Seu nome é tão normal! ')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
   print('Sua média foi boa! PARABÉNS!')
else:
   print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')

# EXERCICIO 28.2

from random import randint
import time
comp = randint(0, 5) #faz com computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jog = int(input('Em que número eu pensei? ')) # O 'jogador' tenta adivinhar
print('PROCESSANDO...')
time.sleep(3)
if jog == comp:
   print('PARABÉNS! Você conseguiu me vencer!')
else:
  print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, jog))