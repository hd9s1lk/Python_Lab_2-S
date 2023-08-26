#Faça um programa python que leia a partir do utilizador 30 números inteiros positivos e 
#que apresente o menor deles


i=0
num=[]

while(i!=3):   
    x = int(input("Insira um número: "))
    num.append(x)
    i+=1
    a = min(num)

print("O número mais pequeno foi: %d" %(a))