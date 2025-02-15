#EXERCICIO 36

v = float(input('Insira o valor da casa: R$'))
s = float(input('Insira o valor do seu salário: R$'))
a = float(input('Em quantos anos você deseja pagar o imóvel? '))
m = s * (30 / 100)
prestação = v / (a*12)
if prestação <= m:
   print('PARABÉNS! O seu empréstimo poderá ser aprovado!')
   print('Para pagar uma casa de R${:.2f} em {} anos'.format(v,a), end='')
   print(' o valor da prestação ficou de R${:.2f}'.format(prestação))
else:
   print('Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(v,a,prestação))
   print('Me despulpe, infelizmente o empréstimo foi NEGADO. Tente novamente em outro momento!')