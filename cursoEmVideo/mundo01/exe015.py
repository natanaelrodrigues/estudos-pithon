# Escreva um program que pergunte a quantidade de km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

dias = int(input('Informe a quantidade de dias de alguel: '))
km = float(input('Informe a quantidade de km percorridos durante o aluguel: '))


vlKm = km * .15
vlDias = dias * 60

print('O Valor do luguel a pagar é de R${:.2f}'.format(vlKm + vlDias))