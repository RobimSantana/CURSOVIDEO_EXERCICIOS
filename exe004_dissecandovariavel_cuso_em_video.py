# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA
# O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES SOBRE ELE

n1 = input("DIGITE ALGO: ")

#podemos utilizar o .format, porem temos que usar as {} dentro das "",ex:
print("O tipo primitivo desse valor é {}".format(type(n1)))
#ou podemos utilizar sem o .format ex:
print("O tipo primitivo desse valor é ", type(n1))
print('Só tem espaços? ', n1.isspace())
print('É um numero? ',n1.isnumeric())
print('É alfabetico? ', n1.isalpha())
print('É alfanumeirco? ',n1.isalnum())
print('Esta maiuscula?', n1.isupper())
print('Esta menuscula? ',n1.islower())
print('Esta capitalizada? ',n1.istitle())


