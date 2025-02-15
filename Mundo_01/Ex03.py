#EXERCICIO 03

#VARIAÇÃO 01

primeiro_numero = int(input("Digite um número"))
segundo_numero = int(input("Digite outro número"))
soma = primeiro_numero + segundo_numero
print('Valor da soma: ', soma) 

#VARIAÇÃO 02

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#VARIAÇÃO 03

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d)) 

#Se quiser continuar na mesma linha coloque (, end= ' ') dentro do segundo parenteses.

print('Divisão inteira {} e a potência {}'.format(di,e))
