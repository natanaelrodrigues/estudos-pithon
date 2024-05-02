'''
Faça um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um triangulo retângulo. calcule e mostre o 
comprimento da hipotenusa.
'''

from math import hypot;

op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))

#hipotenusa = (op ** 2 + ad ** 2) ** (1/2);
hipotenusa = hypot(op, ad);

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))