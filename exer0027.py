#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
#MONSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE
#EX: ANA MARIA DE SOUZA
#PRIMEIRO: ANA
#ULTIMO: SOUZA

n = str(input('Qual é o seu nome completo?: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))
