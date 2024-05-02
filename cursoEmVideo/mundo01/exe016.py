# Crie um programa que leia um número real qualquer pelo teclado e mostre
# sua porção inteira

import math;

num = float(input('Digite um número: '))
porte = math.floor(num)

print('O número {} tem a porte inteira {}'.format(num, porte))

