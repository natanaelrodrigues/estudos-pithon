# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Informe o salário do funcionário: R$'))
novoSal = salario * 1.15

print('O salário R$ {:.2f} com 15% de aumento será de R$ {:.2f}'.format(salario, novoSal))