#Elabore um programa que conte os números pares entre dois números quaisquer.



a = int(input("Insira um numero: \n"))
b = int(input("Insira um segundo numero: \n"))
cont = 0

for i in range(a,b+1):
    if(i % 2 == 0):
        cont= cont +1

print(cont)