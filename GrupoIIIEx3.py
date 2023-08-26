#Elabore um programa python que permita encontrar o maior de um conjunto de números 
#gerados aleatoriamente. A geração deve terminar quando for gerado um múltiplo de 7. 
#Apresente o maior número e quantos números foram gerados.
import random

i=0
num = []

x = random.randint(1,100)
while(x %7 != 0):
    x = random.randint(1,100)
    print(x)
    num.append(x)
    i+=1
    a = max(num)


print("O maior número foi: %d" %(a))
print("Foram gerados: %d" %(i))
        


