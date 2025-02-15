def terreno(l, c):
    a = largura * comprimento 
    print(f'A área de um terreno de {largura} x {comprimento} é de {a}m².')

print('CONTROLE DE TERRENOS')
print('-' *20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
terreno(largura, comprimento)