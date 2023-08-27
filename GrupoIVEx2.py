#Faça um programa que calcule a velocidade média de um veículo em (Km/h). Para tal o 
#utilizador deverá introduzir a distância percorrida (em Km) e o tempo gasto a percorrer 
#essa distância (em minutos). 

km = int(input("Insira o número de Km's que percorreu: "))
minutos = float(input("Insira o número de minutos que demorou: "))

horas = minutos / 60
final = float(km / horas)

print("A sua velocidade final foi de: %f" %(final))