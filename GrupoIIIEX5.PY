#Elabore um programa python que permita encontrar o maior e menor número de uma 
#série de números positivos fornecidos (deve parar quando for introduzido -1).

num=[]

x = 0

while(x!=-1):
    x = int(input("Insira um número: "))
    if x != -1:
        num.append(x)
    if x == -1:
        print("O Programa terminou!")
    
a = max(num)
b = min(num)

print("Máximo: %d" %(a))
print("Mínimo: %d" %(b))



