'''
Desenvolva um program que leia um comprimento de tres retas e 
diga ao usuário se elas podem ou não formar um triangulo.
'''

print('*'*60)
print('ANALISADOR DE TRIANGULO')
print('*'*60)
r1 = float(input('Informe a reta 1: '))
r2 = float(input('Informe a reta 2: '))
r3 = float(input('Informe a reta 3: '))
print('*'*60)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo.')