#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA,
#SABENDO QUE CADA LITRO DE TINTA, PINTA UMA AREA DE 2M²

alt = float(input("qual a altura da parede? "))
larg = float(input("qual a largura da parede? "))
area = alt * larg
print("sua parede tem a dimenção de {} x {} e a sua area é de {}m²".format(alt ,larg , area))
tinta = area / 2 
print("para pintar sua parede vc precisara de {}lts".format(tinta))


