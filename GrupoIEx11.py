#Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este
#deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou
#igual a 20, este deverá ser apresentado subtraindo-se 5.

num1 = float(input("Insira um valor: \n"))
num2 = float(input("Insira um segundo valor: \n"))

soma = num1 + num2

if (soma>20):
    print(soma+8)
elif(soma<=20):
    print(soma-5)
else:
    print("Insira valores válidos: \n")