# Crie um program que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# considere que U$$ 1.00 = R$ 3.27

carteira = float(input('Informe quanto você tem na carteira em R$: '))

dolar = carteira / 3.27

print('Você pode comprar {:.2f} dolares.'.format(dolar))