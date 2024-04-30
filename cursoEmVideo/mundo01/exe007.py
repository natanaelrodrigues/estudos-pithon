# Desenvolva um programa que leia as duas notas de um aluno e calcule sua média.

nota1 = float(input('Infome a primeira nota: '))
nota2 = float(input('Infome a sugunda nota: '))
media = (nota1 + nota2) / 2;

print('A média de {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))