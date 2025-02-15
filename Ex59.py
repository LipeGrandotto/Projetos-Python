#EXERCICIO 59

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
   print('''    [ 1 ] somar
   [ 2 ] multiplicar
   [ 3 ] maior
   [ 4 ] novos números
   [ 5 ] sair do programa''')
   opçao = int(input('Qual é a sua opção? '))
   if opçao == 1:
       soma = n1 + n2
       print('A soma entre {} e {} é {}'.format(n1, n2, soma))
   elif opçao == 2:
       produto = n1 * n2
       print('O resultado de {} X {} é {}'.format(n1, n2, produto))
   elif opçao == 3:
       if n1 > n2:
           maior = n1
       else:
           maior = n2
       print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
   elif opçao == 4:
       print('Informe os número novamente: ')
       n1 = int(input('Primeiro valor: '))
       n2 = int(input('Segundo valor: '))
   elif opçao == 5:
       print('Finalizando...')
   else:
       print('Opção inválida. Tente novamente')
   print('=-=' * 10)
   sleep(1.5)
print('Fim do programa! Volte sempre! ')