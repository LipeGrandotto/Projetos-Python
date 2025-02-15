from random import randint
num = []

def sorteia(num):
    for c in range(0,5):
        num.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: {num}', flush=True)

def somapar():
    par = []
    for numeros in num:
        if numeros / 2:
            par.append(numeros)
            print(f'Somando os valores pares de {par}, temos {sum(par)}')


sorteia()
somapar()