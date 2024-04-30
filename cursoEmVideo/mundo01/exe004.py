texto = input('Digite algo:');

print('o tipo primitivo deste valor é',type(texto))
print('Só tem espaços?',texto.isspace())
print('E´um Número?',texto.isnumeric())
print('E´um alfabetico?',texto.isalpha())
print('E´um alfanumerico?',texto.isalnum())
print('Está em maiúsculas?',texto.isupper())
print('Está em minúsculas?',texto.islower())
print('Está capitalizada?',texto.istitle())