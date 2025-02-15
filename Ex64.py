# EXERCICIO 64

n = soma = cont = 0
n = int(input('Digite um número : [999 para PARAR]'))
while n != 999:
    cont += 1
    soma += n 
    n = int(input('Digite um número : [999 para PARAR]'))
print('Você digitou {} números.'.format(cont))
print('A soma dos valores é {}.'.format(soma))