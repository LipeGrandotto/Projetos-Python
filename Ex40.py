#EXERCICIO 40

p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
media = (p1 + p2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(p1,p2,media))
if media < 5:
   print('O aluno está REPROVADO!')
elif 7 > media >= 5:
   print('O aluno está de recuperação!')
else:
   print('PARABÉNS! Você foi aprovado!')