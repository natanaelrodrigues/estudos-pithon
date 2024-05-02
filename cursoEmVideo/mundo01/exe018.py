'''
Faça um programa que leia o angulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse angulo.
'''
import math

angulo = float(input('Informe um angulo: '))
radianoAngulo = math.radians(angulo)

seno = math.sin(radianoAngulo)
coss = math.cos(radianoAngulo)
tan = math.tan(radianoAngulo)

print('O seno do angulo {} é {:.2f}.'.format(angulo, seno))
print('O cosseno do angulo {} é {:.2f}.'.format(angulo, coss))
print('A tangente do angulo {} é {:.2f}.'.format(angulo, tan))