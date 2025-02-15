#EXERCICIO 57

g = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while g not in 'MmFf':
   g = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(g))
