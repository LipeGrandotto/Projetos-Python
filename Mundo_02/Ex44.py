#EXERCICIO 44

print('='*10, end='') 
print('LOJAS LUIZ', end='')
print('='*10)
compra = int(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque/PIX
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
vinte = compra * (20 / 100)
dez = compra * (10 / 100)
cinco = compra * (5 / 100)
opcao = int(input('Escolha a sua opção: '))
if opcao == 1:
   print('O valor em dinheiro/cheque/PIX COM DESCONTO DE 10% ficou R${:.2f}'.format(compra - dez))
elif opcao == 2:
   print('O valor à vista no cartão COM DESCONTO DE 5% ficou R${:.2f}'.format(compra - cinco))
elif opcao == 3:
   print('O valor total parcelado em 2x no cartão fica R${}'.format(compra))
   print('O valor da parcela ficou R${:.2f}'.format(compra / 2))
elif opcao == 4:
   parcela = int(input('Você deseja parcelar em quantas vezes? '))
   print('O valor total parcelado em {}x ficou R${:.2f} COM JUROS DE 20%'.format(parcela, compra + vinte))
   print('O valor de cada parcela ficou R${:.2f}'.format((compra + vinte) / parcela))