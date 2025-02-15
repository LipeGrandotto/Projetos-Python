# EXERCICIO 66

n = soma = cont = 0
while True:
    n = int(input('Digite um número : [999 para PARAR]  '))
    if n == 999:
        break
    cont += 1
    soma += n 
print('Você digitou {} valores.'.format(cont))
print('A soma dos valores é {}.'.format(soma))