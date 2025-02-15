def escreva(txt):
    print('-' * (len(texto) + 4))
    print(f'  {txt}')
    print('-' * (len(texto) + 4))


texto = str(input('Escreva seu texto: '))
escreva(texto)