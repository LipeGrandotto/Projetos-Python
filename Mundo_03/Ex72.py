# EXERCICIO 72

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dessoito','dessenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente. ', end=' ')
    else:
        break
print(f'O número que você digitou foi {tupla[n]}.')