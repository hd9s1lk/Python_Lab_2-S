#Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma 
#dos quadrados dos elementos do vetor. 

A = []
quadrados = []

for valores in range(0,2):
    var1 = int(input("Insira valores na lista: "))
    A.append(var1)
    quadrados.append(var1**2)

print(A)
print(quadrados)

soma = sum(quadrados)
print(soma)
