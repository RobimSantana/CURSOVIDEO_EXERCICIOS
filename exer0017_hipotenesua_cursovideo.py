# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E ADJACENTE DE UM TRIANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot
cateto = float(input(" Quanto medi o cateto? "))
adjacent = float(input("Quanto medi o adjacente? "))
hip = hypot(cateto, adjacent)
print("A hipotenusa vai medir {:.2f}".format(hip))





'''CA = float(input("Quanto o Cateto oposto? "))
AD = float(input("Quanto vale o cateto adjacente? "))
HP = (CA** 2 + AD** 2)** (1/2)
print(" A hipotenusa vale {:.2f}".format(HP))'''




      





