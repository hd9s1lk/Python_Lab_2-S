#Elabore um programa que receba uma frase e conte o número de vogais existente na frase.

frase=input("Insira uma frase")
cont=0
for c in frase.lower():
    if c in ['a','e','i','o','u']:
        cont += 1
print("Foram encontradas",cont,"Vogais")