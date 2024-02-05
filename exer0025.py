# Crie um programa que leia o nome de uma pessoa e diga se la 
# tem ou não 'SILVA' no nome

nome = str(input('Qual é o seu nome completo?: ')).strip()
print('Seu nome tem Silva? {}'.format ('silva' in nome.lower()))
