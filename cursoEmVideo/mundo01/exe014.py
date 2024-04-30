# Faça um programa que leia a temperatura em °C e demonstre em °F

cel = float(input('Qual a tempoeratura em °C:'))

f = ((9 * cel) /5) + 32;

print('A temperatura em {:.1f} °C corresponde em {:.1f} °F'.format(cel, f))
