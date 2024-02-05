# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS
# FAÇA UM PROGRAMA QUE LEIA O nome DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA


"""n1 = input(" primeiro aluno?: ")
n2 = input(" segundo aluno?: ")
n3 = input(" terceiro aluno?: ")
n4 = input("quanrto aluno?; ")

lista = [n1, n2 ,n3, n4] 
sorteio = sorted(lista)

print(" segue a ordem dos alunos{}".format(sorteio))"""


import random

n1 = input(" primeiro luno: ")
n2 = input("segundo aluno: ")
n3 = input("terceior aluno:")
n4 = input("quarto aluno: ")

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(" a ordem ficará{}".format(lista))
