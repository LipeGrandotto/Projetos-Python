# EXERCICIO 12

s = float(input('Qual é o salário do Funcionário? R$'))
a = s + (s * 15 /100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(s,a))