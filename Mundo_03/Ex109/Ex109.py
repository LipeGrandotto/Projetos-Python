import moeda

preco = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa oferecida: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Diminuindo em {moeda.taxas(taxa)}, temos {moeda.deficit(preco, taxa, True)}') 
print(f'Aumentando em {moeda.taxas(taxa)}, temos {moeda.aumento(preco, taxa, True)}')