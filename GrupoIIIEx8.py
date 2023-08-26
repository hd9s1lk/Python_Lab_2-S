#Elabore um programa python que permita calcular a soma dos 20 primeiros números 
#pares positivos.

num = 0
total = 0

for num in range(1,20):
    if (num%2 == 0):
        total += num

print(total)