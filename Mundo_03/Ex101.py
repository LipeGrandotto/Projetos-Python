# def par (n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# while True:
#     num = int(input('Digite um número: '))
#     resp = input('Deseja escrever outro número? ').upper().strip()[0]
#     if par(num):
#         print(f'O número {num} é par !')
#     else:
#         print(f'O número {num} é ímpar !') 
#     if resp == 'N':
#         break


def voto ():
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade < 60:
        print(f'Com {idade} anos: SEU VOTO É OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos: SEU VOTO É OPCIONAL.')

# PROGRAMA PRINCIPAL
print('-=' * 28)
nascimento = int(input('Em que ano você nasceu? '))
voto()