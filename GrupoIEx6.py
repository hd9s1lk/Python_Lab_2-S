#Implemente um programa python que indique se um dado número inteiro é PAR ou
#ÍMPAR.

num = int(input("Insira um numero: \n"))

if (num<0):
    print("ERRO")
elif (num % 2 == 0):
    print("%d é par\n" %(num))
elif(num % 2 != 0):
    print("%d é ímpar\n" %(num))
else:
    print("Insira um valor válido: \n")