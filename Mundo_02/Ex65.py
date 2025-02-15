# EXERCICIO 65 FOI

cont = 0
soma = 0
maior = 0
menor = 0
afirmacao = 'Ss'
while afirmacao != 'N':
    n = int(input('Digite um número: '))
    afirmacao = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    cont += 1
    soma += n
    menor = n
    if afirmacao == "N":
        media = soma / cont
        print('Você digitou {} números e a média é {}.'.format(cont, media))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('O maior número foi {} e o menor foi {}.'.format(maior, menor))
