import moeda

preco = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa oferecida: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando em {moeda.taxas(taxa)}, temos {moeda.moeda(moeda.aumento(preco, taxa))}')
print(f'Diminuindo em {moeda.taxas(taxa)}, temos {moeda.moeda(moeda.deficit(preco, taxa))}') 