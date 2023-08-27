#Faça um algoritmo que sendo dada a medida de 2 catetos de um triângulo retângulo, 
#calcule a medida da hipotenusa. 
import math as m

cat1 = float(input("Insira a medida de um cateto: "))
cat2 = float(input("Insira a medida de um cateto: "))
hip = float(m.sqrt(pow(cat1,2) + pow(cat2,2)))

print("A medida da hipotenusa é de: %f" %(hip))
