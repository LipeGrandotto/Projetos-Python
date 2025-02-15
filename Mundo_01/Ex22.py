# EXERCICIO 22

frase = 'Curso em Video Python'
frase = 'Curso em Video Python'
print(frase[::2])

frase = 'Curso em Video Python'
print(frase.count('o'))

frase = 'Curso em Video Python'
print(frase.upper().count('O'))

frase = 'Curso em Video Python'
print(len(frase)) #frase.strip() Retira os espaços da frente e de trás da frase.

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))

frase = 'Curso em Video Python'
print(frase.find('Video'))

frase = 'Curso em Video Python'
print(frase.split())

frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[0][3])

# Para uma frase grande coloque print("""     texto      """)
print("""fnsdfnysfynsfynsfynsyfjnbadfbadbarghbatrbhERBAE
ABAERTBAERBASETHBAETHNASTHJYT
THATHJATHHATHATEHJATJA
ATHARTJATJHAR6JATJHATHAT5H@!""")

#EXERCICIO 22.2

frase = 'Curso em Video Python'
print(frase.upper())

frase = 'Curso em Video Python'
print(frase.lower())

frase = 'Curso em Video Python'
print(len(frase) - frase.count(' '))

frase = 'Curso em Video Python'
dividido = frase.split()
print(len(dividido[0]))

nome = input('Digite seu nome completo: ') .strip()
print('Analisando seu nome... ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu none tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))