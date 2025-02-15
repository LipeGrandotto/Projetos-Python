def dobro(p = 0, formato=False):
    result = p * 2
    return result if formato is False else moeda(result)


def metade (p = 0, formato=False):
    result = p / 2
    return result if formato is False else moeda(result)


def aumento (p = 0, tx = 0, formato=False):
    result = p + (p * tx/100)
    return result if formato is False else moeda(result)


def deficit (p = 0, tx = 0, formato=False):
    result = p - (p * tx/100)
    return result if formato is False else moeda(result)


def moeda (p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def taxas (p = 0, taxas = '%'):
    return f'{p}{taxas}'