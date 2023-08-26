#Dada uma série de 20 valores reais no intervalo [0, 15], faça um programa python que 
#calcule e escreva a média aritmética destes valores. Entretanto se a média obtida for 
#maior que 8 deverá ser atribuída 10 para a média.

i=0
num =[]

while(i!=3):
    x = int(input("Insira um número entre 0 e 15: "))
    num.append(x)
    total = sum(num)
    i+=1

media = float(total / len(num))

if media >= 8:
    print("Valor atribuído: 10")
else:
    print("Valor atribuído: %f" %(media))



