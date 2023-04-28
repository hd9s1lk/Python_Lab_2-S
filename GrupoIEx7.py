# Elabore um programa que de entre dois números fornecidos pelo utilizador, permita
#encontrar o menor deles.

num1 = float(input("Insira um primeiro numero: \n"))
num2 = float(input("Insira um segundo numero: \n"))

if(num1>num2):
    print("%f é maior\n" %(num1))
elif(num2>num1):
    print("%f é maior\n" %(num2))
else:
    print("Insira valores válidos\n")