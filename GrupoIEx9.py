#Elabore um programa python que permita, através da inserção dos lados de um
#triângulo, identificar de que tipo de triângulo se trata (isósceles – dois lados iguais e
#um diferente, equilátero – todos os lados iguais, escaleno – se todos os lados forem
#diferentes).

lado1 = float(input("Insira um lado de um triângulo: \n"))
lado2 = float(input("Insira um lado de um triângulo: \n"))
lado3 = float(input("Insira um lado de um triângulo: \n"))

if (lado1 == lado2 and lado1 == lado3):
    print("Triângulo equilátero\n")
elif(lado1 == lado2  and lado1 != lado3):
    print("Triângulo isósceles\n")
elif(lado2 == lado3 and lado2 != lado1):
    print("Triângulo isósceles\n")
elif(lado3 == lado1 and lado3 != lado2):
    print("Triângulo isósceles\n")
elif(lado1 != lado2 and lado2 != lado3):
    print("Triângulo escaleno\n")