def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mERRO! Entrada de dados interrompida pelo usuário!\033[m')
            break
        else: 
            return num


def leiafloat(msg):
    while True:
        try:
            entrada = input(msg).replace(',','.').strip()
            num = float(entrada)
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mERRO! Entrada de dados interrompida pelo usuário!\033[m')
            break
        else:
            return num


nint = leiaint('Digite um número inteiro: ')
nreal = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {nreal}')