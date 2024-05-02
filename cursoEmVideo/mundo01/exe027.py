'''
Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = str(input('Informe seu nome completo: ')).strip().split();
print('ANALISANDO SEU NOME')
print('='*40)
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))