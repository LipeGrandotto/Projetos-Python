#EXERCICIO 42

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Insira o valor do primeiro segmento: '))
r2 = float(input('Insira o valor do segundo segmento: '))
r3 = float(input('Insira o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
   if r1 == r2 == r3:
       print('EQUILÁTERO!')
   elif r1 != r2 != r3 != r1:
       print('ESCALENO!')
   else:
       print('ISÓSCELES!')
else:
   print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')