def maior():
    print('Analisando os valores passados...')
    numeros.sort()
    print(numeros)
    print(f'Foram informados {len(numeros)} números.')
    print(f'O maior valor informado foi {numeros[-1]}')


def lin():
    print('-=' * 28)


numeros = []
while True:
    quant = int(input('Deseja informar quantos números? '))
    for c in range(1, quant + 1):
        numeros.append(int(input(f'Informe o {c}º número: ')))
    opc = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
lin()
maior()
lin()