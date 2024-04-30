primeiro = int(input('Informe o primeiro número:'))
segundo = int(input('Informe o segundo número:'))

if primeiro > segundo:
    print('o primeiro é maior')
else:
    print('o segundo é maior')



idade = int(input('Informe sua idade:'))

if idade < 18:
    print('Você é menor de idade')
elif idade < 60:
    print('Você está na fase da meia idade')
else:
    print('Você chegou a 3° idade')