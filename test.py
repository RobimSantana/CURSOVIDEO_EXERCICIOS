n1=int(input('numero: '))
n2=int(input('numero: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2
print('='*10,'robim','='*10)
print(f'a soma é {s:=^10} \nO pruduto é {m:=^10} \nA divisão é {d:.2f}\n',end="")
print('divisão inteira {} e a potencia é {}'.format(di, e))
print("="*20)