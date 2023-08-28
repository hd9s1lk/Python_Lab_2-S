#Elabore um programa que tenha como entrada um vetor (cujos elementos são do tipo 
#inteiro) e forneça como saída a média aritmética dos números do vetor.

A = []

length = int(input("Defina o tamanho da sua lista: "))

for num in range(0,length):
    var = int(input("Insira números na sua lista: "))
    A.append(var)
print(A)

media = float(sum(A) / len(A))

print("Média final: %f" %(media))