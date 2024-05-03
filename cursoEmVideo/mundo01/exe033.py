'''
Faça um programa que leia três números e 
mostre qual é o maior e qual é o menor.
'''

num1 = int(input('Informe o númerio 1: '))
num2 = int(input('Informe o númerio 2: '))
num3 = int(input('Informe o númerio 3: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O maior número é {} e o menor número é o {}'.format(maior, menor))    