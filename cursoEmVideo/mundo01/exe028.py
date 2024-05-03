'''
Escreva um programa que faça o computador "pensar" em um número 
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual 
foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep

computador = randint(0,5)
print('='*60)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('='*60)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('PARABENS!!! Você conseguiu me vencer!')
else:
    print('QUE PENA! Eu venci! Eu pensei no número {} e não no {}.'.format(computador, jogador))