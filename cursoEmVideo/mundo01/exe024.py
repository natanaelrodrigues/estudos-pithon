'''
Crie um programa que leia o nome de uma cidade e diga se 
ela começa com o nome "SANTO"
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip();
print(cidade.split()[0].upper() == 'SANTO')