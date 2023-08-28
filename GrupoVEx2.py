#Elabore um programa que ao ler duas listas A e B com N e M elementos, respetivamente:
#a. gere uma nova lista C que corresponde à união das listas A e B.
#b. imprima as listas A, B e C

A = []
B = []
C = []

array1 = int(input("Defina o tamanho da sua lista A: "))

for nums in range(1,array1 +1):
    var1 = int(input("Insira valores para a lista A: "))
    A.append(var1)
print(A)

array2 = int(input("Defina o tamanho da sua lista B: "))

for nums1 in range(1,array2+1):
    var2 = int(input("Insira valores para a lista B: "))
    B.append(var2)
print(B)

C = A + B

print("Produto Final: \n")
print(A)
print(B)
print(C)




