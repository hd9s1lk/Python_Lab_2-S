#Faça um programa que leia um vetor de 5 números inteiros e que apresente a soma e a 
#multiplicação desses números. 

A = []


for num in range(0,5):
    var1 = int(input("Escreva um número: "))
    A.append(var1)
    final = 1
    for nums in A:
        final = final * nums

Sum = sum(A)
print(Sum)
print(final)



