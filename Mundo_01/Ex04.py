#EXERCICIO 04

n = input('Digite algo: ')
print(n.isdecimal())

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços: ', a.isspace())
print('É númerico: ', a.isalpha())
print('É alfanúmero: ', a.isalnum())
print('Só tem letras maiusculas: ', a.isupper())
print('Só tem letras minusculas: ', a.islower())
print('É capitalizada: ', a.istitle())