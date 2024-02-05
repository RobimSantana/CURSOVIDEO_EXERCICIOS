# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO, FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O nome DELES E ESCREVENDO
# O nome DO ESCOLHIDO NA TELA.


"""from math import random 
n1 = str(input(" Primeiro aluno : "))
n2 = str(input(" Segundo aluno : "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
M = (n1* n2* n3* n4)

print(" O ALUNO SORTEADO FOI O {}".format(random(M)))"""

# import random
from random import choice

n1 = str(input("primeiro aluno ? "))
n2 = str(input(" segundo aluno ? "))
n3 = str(input("terceiro aluno? "))
n4 = str(input("quarto aluno? "))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print(" o aluno sorteado foi o {}".format(sorteado))
