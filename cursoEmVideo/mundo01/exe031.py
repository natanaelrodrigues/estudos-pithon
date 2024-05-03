'''
Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem. Cobrando R$0,50 por km para 
viagens até 200km e R$0,45 para viagens mais longas.
'''

km = float(input('Qual é a distância da sua viagem? '));
print('Você está prestes a começar uma viagem de {}km.'.format(km));
print('E o preço da sua passagem será de R$ {:.2f}'.format(km * .5 if km<= 200 else km *.45))