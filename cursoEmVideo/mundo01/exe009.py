#Faça um programa que leia um número inteiro qualuqer e mostre sua taboada:


num = int(input('Digite um dúmero para a taboada: '))

i = 0
print('*'*20)
while i <= 11:
    print('{} X {:2} = {:3}'.format(num,i,num*i))
    i += 1
print('='*20)