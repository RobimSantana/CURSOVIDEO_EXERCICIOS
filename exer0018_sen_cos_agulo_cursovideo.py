# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGUENTE DE ANGULO

'''import math
ag = float(input("qual o angulo? "))
se = math.sin(ag)
co = math.cos(ag)
ta = math.tan(ag)
print(" O SENO {:.2f}, COSSENO {:2f}, TANGENTE {:2f}".format(se, co, ta))'''


'''import math
ag = float(input(" qual o angulo: "))
sen = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tan = math.tan(math.radians(ag)) 
print( " o valor do cosseno é {:.2f},  o valor do cosseno é {:.2f}, o valor da tangente é {:.2f} ".format(sen, cos, tan))'''


from math import radians, cos, sin, tan
ag = float(input(" qual o angulo: "))
sen = sin(radians(ag))
cos = cos(radians(ag))
tan = tan(radians(ag)) 
print( " o valor do cosseno é {:.2f},  o valor do cosseno é {:.2f}, o valor da tangente é {:.2f} ".format(sen, cos, tan))