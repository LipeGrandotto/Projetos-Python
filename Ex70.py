# EXERCICIO 70

print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)
soma = contp = precom = cont = 0
barato = ' '
while True:
    p = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    soma += preco
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar?  [S/N] ')).strip().upper()[0] 
    if preco > 1000:
        contp += 1
    if cont == 1 or preco < precom:
        precom = preco
        barato = p
    if pergunta == 'N':
        break
print('-'*10,' FIM DO PROGRAMA ','-'*10)
print(f'O total da compra foi R${soma:.2f}.')
print(f'Temos {contp} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi a(o) {barato} que custa R${precom:.2f}')