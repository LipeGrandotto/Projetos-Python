def leiaint(msg):
    ok = False
    n = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro valido!\033[m')
        if ok:
            break
    return valor



n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')