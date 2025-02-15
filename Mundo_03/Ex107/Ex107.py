import moeda

preco = float(input('Digite o preço: R$ '))
taxa = float(input('Digite a taxa oferecida: '))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando em {taxa}%, temos R${moeda.aumento(preco, taxa)}')
print(f'Diminuindo em {taxa}%, temos R${moeda.deficit(preco, taxa)}')