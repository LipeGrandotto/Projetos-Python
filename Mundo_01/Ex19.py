#EXERCICIO 19 

import random
p1 = input('Primeiro nome: ')
p2 = input('Segundo nome: ')
p3 = input('Terceiro nome: ')
p4 = input('Quarto nome: ')
lista = [p1, p2, p3, p4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))