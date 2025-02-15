#EXERCICIO 14

d = int(input('Quantos dias alugados? '))
k = float(input('Quantos KM você rodados? '))
p = (d * 60) + (k * 0.15)
print('O valor á pagar é de R${:.2f}'.format(p))