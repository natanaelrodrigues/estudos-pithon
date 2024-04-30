# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule a sua area e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m2

largura = float(input('Informe a largura da parede: '))
altura  = float(input('Informe a altura da parede: '))
area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua area é de {}m2.'.format(largura, altura, area))
tinta  = area / 2
print('Para pintar esta area, você precisará de {} litros de tinta.'.format(tinta))