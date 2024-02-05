# FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA
#CADA UM DOS DIGITOS SEPARADOS 

numero=int(input('Digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'ANALISANDO O NUMERO {numero}')
print(f'UNIDADE: {u}')
print(f'DEZENA: {d}')
print(f'CENTRENA: {c}')
print(f'MILHAR: {m}')