'''
Crie um programa que leia o nome completo de umapessoa e mostre:
O nome com todos as letras maiúsculas e minusculas
Quantas letras ao todo(sem considerar os espaços)
Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
print('O nome em CAIXA ALTA é {}.'.format(nome.upper()))
print('O nome em CAIXA BAIXA é {}.'.format(nome.lower()))
print('O nome em possui {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome em possui {} letras.'.format(len(nome.split()[0])))