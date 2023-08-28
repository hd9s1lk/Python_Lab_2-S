#Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram 
#lidas. Imprima as consoantes.

A = []
i=0

for letter in range(0,10):
    var = input("Insira letras nesta lista: ")
    A.append(var)
    if var != "a" and var != "e" and var != "i" and var != "o" and var != "u":
        i+=1 

print(i) 