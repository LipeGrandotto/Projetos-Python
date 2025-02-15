# EXERCICIO 94

dic = {}
somaidade = []
mulheres = []
cont = 0
lista = []
while True:
    nome = str(input('Nome: '))
    cont += 1
    sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if sexo not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo in 'Ff':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    somaidade.append(idade)
    dic [nome] = [idade, sexo]
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
soma = sum(somaidade)
media = soma / cont
print()
print('-=' * 28)
print()
print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
print(f'B)  A média de idade é de {media:5.2f} anos.')
print(f'C)  As mulheres cadastradas foram {", ".join(mulheres)}')
print(f'D)  Lista das pessoas que estão acima da média: ')
for k, v in dic.items():
    if v[0] > media:
        print() 
        print(f'Nome: {k} \nIdade: {v[0]} \nSexo: {v[1]}')  
print()    
print('<<< ENCERRADO >>>')
