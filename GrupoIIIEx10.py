#Faça um programa python para ler a base e a altura de 50 triângulos e imprimir a sua área.

i=0

while(i!=3):
    a = float(input("Insira a base do triângulo: "))
    b = float(input("Insira a altura do triângulo: "))
    total = float((a*b)/2)
    print("A área do triângulo é de: %f" %(total))
    i+=1