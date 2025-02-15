def resumo (preco, tx01, tx02):
    lin('RESUMO DE VALOR'.center(34))
    print(f'PREÇO ANALISADO: \t{moeda(preco)}')
    print(f'DOBRO DO PREÇO: \t{dobro(preco, True)}')
    print(F'METADE DO PREÇO: \t{metade(preco, True)}')
    print(f'{taxas(tx01)} DE AUMENTO: \t{aumento(preco, tx01, True)}')
    print(f'{taxas(tx02)} DE REDUÇÃO: \t{deficit(preco, tx02, True)}')
    print('-' * 34)


def lin(msg):
    print('-' * 34)
    print(msg)
    print('-' * 34)

def dobro(p = 0, formato=False):
    result = p * 2
    return result if formato is False else moeda(result)


def metade (p = 0, formato=False):
    result = p / 2
    return result if formato is False else moeda(result)


def moeda (p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def aumento (p = 0, tx = 0, formato=False):
    result = p + (p * tx/100)
    return result if formato is False else moeda(result)


def deficit (p = 0, tx = 0, formato=False):
    result = p - (p * tx/100)
    return result if formato is False else moeda(result)


def taxas (p = 0, taxas = '%'):
    return f'{p}{taxas}'