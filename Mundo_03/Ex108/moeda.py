def dobro(p = 0):
    result = p * 2
    return result


def metade (p = 0):
    result = p / 2
    return result


def aumento (p = 0, tx = 0):
    result = p + (p * tx/100)
    return result


def deficit (p = 0, tx = 0):
    result = p - (p * tx/100)
    return result


def moeda (p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def taxas (p = 0, taxas = '%'):
    return f'{p}{taxas}'