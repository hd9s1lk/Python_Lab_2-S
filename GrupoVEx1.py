#Elabore um programa que permita ler valores para uma lista A de dimensão 10:
#a. altere a lista A invertendo a ordem dos elementos (trocar a1 por a10, ...)
#b. imprima a nova lista A.
#c. altere o programa de forma que o vetor tenha dimensão 100.

num=[] 

for nums in range(1,11):
    nums = int(input("Insira valores para a lista: "))
    num.append(nums)

print(num)

rev = num.reverse()

print(num)

#dimensão 100 alterar o ciclo for
