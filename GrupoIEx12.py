# Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a
#zero e o quadrado do número caso ele seja negativo.

import math as m

num = float(input("Insira um valor: \n"))

if(num>=0):
    print(m.sqrt(num))
elif(num<0):
    print(num*num)
else:
    print("Insira valores válidos\n")