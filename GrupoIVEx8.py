#Dada uma determinada quantidade em dinheiro correspondente a um número inteiro de 
#euros, determine o menor número de moedas e notas que perfaz essa quantia (considerar 
#apenas os valores de 1, 2, 5, 10, 20 e 50 €). 

conta = float(input("Insira a sua conta final: "))

var1 = int(conta /50) #Número de notas de 50
conta_1 = int(conta - (var1*50)) #Resto da conta

var2 = int(conta_1 /20) #Número de notas de 20
conta_2 = int(conta_1 -(var2*20)) #Resto da conta

var3 = int(conta_2 /10) #Número de notas de 10
conta_3 = int(conta_2 -(var3*10)) #Resto da conta

var4 = int(conta_3 /5) #Número de moedas de 5
conta_4 = int(conta_3 -(var4*5)) #Resto da conta

var5 = int(conta_4 /2) #Número de moedas de 2
conta_5 = int(conta_4 -(var5*2)) #Resto da conta

if (conta_5 < 1):
    var6 = 0
else:
    var6 = int(conta_5 /1) #Número de moedas de 1
    conta_6 = int(conta_4 -(var6*1)) #Resto da conta



print("Notas de 50€: %f" %(var1))
print("Notas de 20€: %f" %(var2))
print("Notas de 10€: %f" %(var3))
print("Notas de 5€: %f" %(var4))
print("Notas de 2€: %f" %(var5))
print("Notas de 1€: %f" %(var6))
