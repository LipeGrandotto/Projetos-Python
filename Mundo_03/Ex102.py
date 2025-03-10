def fatorial(n=0, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """


    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# PROGRAMA PRINCIPAL   
n = int(input('Digite um número para calculcar seu Fatorial: '))
show = str(input('Você deseja que apareça o processo? [S/N] ')).strip().upper()[0]
if show == 'S':
    show=True
else:
    show=False
print(fatorial(n, show))
help(fatorial)  