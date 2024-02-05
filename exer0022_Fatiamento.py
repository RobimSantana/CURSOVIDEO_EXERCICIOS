# CREI UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIUSCULAS
# O NOME COM TODAS AS LETRAS  MENUSCULAS
# QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
# QUANTAS TEM O PRIMEIRO NOME

nome= str(input('QUAL O SEU NOME COMPLETO?: ')).strip()
print('ANALISANDO SEU NOME....')
print('Seu nome em maiusculo {}'.format(nome.upper()))
print(f'Seu nome em menusculo é {nome}'.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome. count(' ')))
print('Seu primeiro nome tem {} letars'.format(nome.find(' ')))

#separa=nome.strip()
#print('Seu primeiro nome é {} e tem {} letras'.format((separa[0],len(separa[0]))))
#Robson Santana De Oliveira