#EXERCICIO 29

vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
   print('MULTADO! Você excedeu o limite permitidido que é de 80Km/h')
   print('Você deve pagar uma multa de R${:.2f}!'.format((vel-80)*7))
else:
   print('Tenha um bom dia! Dirija com segurança!')