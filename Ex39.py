#EXERCICIO 39

from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
maiorid = idade - 18
previsao = ano + maiorid
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if idade < 18:
  print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
   print('Seu alistamento será este ano! Se aliste IMEDIATAMENTE!')
elif idade > 18:
   print('Seu alistamento já deveria ter sido feito há {} anos'.format(maiorid))
   print('Seu alistamento foi em {}'.format(atual - maiorid))
