#Dado um valor horário em horas, minutos e segundos, calcule o número de segundos 
#totais. 

hora = int(input("Insira o número de horas: "))
hora_s = hora * 60 * 60

minu = int(input("Insira o número de minutos: "))
minu_s = minu * 60 

seg = int(input("Insira o número de segundos: "))

total = float(hora_s + minu_s + seg)

print("Valor final: %d" %(total))