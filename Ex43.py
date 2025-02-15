# EXERCICIO 43

peso = float(input('Qual é seu peso? (Kg) '))
altu = float(input('Qual é sua altura? (m) '))
imc = peso /(altu**2)
if imc < 18.5:
   print('Seu IMC é {:.2f}, você está ABAIXO DO PESO!'.format(imc))
elif imc < 25:
   print('Seu IMC é {:.2f}, você está no PESO IDEAL!'.format(imc))
elif imc < 30:
   print('Seu IMC é {:.2f}, você está no SOBREPESO!'.format(imc))
elif imc < 40:
   print('Seu IMC é {:.2f}, você está no OBESIDADE!'.format(imc))
elif imc > 40:
   print('Seu IMC é {:.2f}, você está no OBESIDADE MÓRBIDA!'.format(imc))