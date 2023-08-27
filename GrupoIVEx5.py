#Dado um ângulo em graus, efetue a sua conversão para radianos. 
import math as m

angulo = float(input("Insira uma medida de um ângulo: "))

final = float(angulo * (m.pi / 180))

print("Valor em radianos: %f" %(final))

