# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

preco = float(input('Informe o preço do produto: '))
liq = preco * .95

print('O produto com 5% de desconto é {:.2f}'.format(liq))