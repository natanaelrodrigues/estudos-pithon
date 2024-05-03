'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h. Mostre uma menasgem dizendo
que ele foi multado.
A multa vai custar R$7 por cda km acima do limite.
'''

km = float(input('Informe a velocidade atual: '))

if km > 80:
    print('VOCÊ FOI MULTADO')
    print('Sua multa foi de R${:.2f}.'.format((km-80) * 7))
else:
    print('Tenha um bom dia! Diriga com segurança')