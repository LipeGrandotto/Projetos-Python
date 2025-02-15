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


def lin ():
    print('-' * 42)


def titulo(msg):
    lin()
    print(msg.center(42))
    lin()


def cabecalho(menu):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in menu:
        print(f'\033[33m{c}\033[m - \033[034m{item}\033[m')
        c += 1
    lin()
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc