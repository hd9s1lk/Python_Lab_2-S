#Faça um programa que leia 20 números inteiros e que os armazene num vetor. Armazene 
#os números pares no vetor PAR e os números ímpares no vetor IMPAR. Imprima os três 
#vetores.

total = []
par = []
impar = []

for num in range(0,5):
    var1 = int(input("Insira números na lista: "))
    total.append(var1)
    if var1 %2 == 0:
        par.append(var1)
    if var1 %2 !=0:
        impar.append(var1)

print(total)
print(par)
print(impar)


