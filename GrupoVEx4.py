#Elabore um programa que tenha como entrada um vetor (cujos elementos são do tipo 
#real) e forneça como saída o menor elemento do vetor.

A = []

length = int(input("Defina o tamanho da sua lista: "))

for num in range(0, length):
    var = float(input("Insira números na lista: "))
    A.append(var)

pequeno = min(A)
print(pequeno)
