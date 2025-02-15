# EXERCICIO 68

from random import randint
cont = 0
while True:
    print('-=' *25)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' *25)
    n = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print(f'Você jogou {n} e o computador {computador}. Total de {total}')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR') 
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            cont += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            cont += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
