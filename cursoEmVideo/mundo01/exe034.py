'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor de seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento será de 15%
'''

sal = float(input('Informe o salário do funcionário: '))

if(sal <= 1250):
    novo = sal*1.15
else:
    novo = sal*1.10

print('O novo salario será de {:.2f}'.format(novo))