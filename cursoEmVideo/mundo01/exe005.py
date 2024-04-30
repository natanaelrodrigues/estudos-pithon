# Faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.

num = int(input('Informe um número: '))

ant = num - 1
suc = num + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(num, ant, suc))