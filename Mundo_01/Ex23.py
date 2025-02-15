# EXERCICIO 23

# Modo não total, ele não reconhece caso o digito não tenha os 4 digitos

n = int(input('Informe um número: '))
num = str(n)
print('Analisando o número {}'.format(num))
print('Unidade{}'.format(num[3]))
print('Dezena {}'.format(num[2]))
print('Centena {}'.format(num[1]))
print('Milhar {}'.format(num[0]))

# Versão completa

n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
