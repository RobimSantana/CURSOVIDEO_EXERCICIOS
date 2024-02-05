# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE
# E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

cid = str(input('Qual a sua cidade?: ')).strip()
print(cid [:5].upper() == 'SANTO')