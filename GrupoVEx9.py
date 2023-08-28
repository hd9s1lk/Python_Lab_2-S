#Faça um programa que peça a idade e a altura de 5 pessoas e que armazene cada 
#informação no seu respetivo vetor. Imprima a idade e a altura na ordem inversa da ordem 
#lida.

age = []
height = []

for valores in range(0,2):
    var1 = int(input("Insira a sua idade: "))
    age.append(var1)
    var2 = float(input("Insira a sua altura: "))
    height.append(var2)
print(age)
print(height)

age.reverse()
height.reverse()

print(age)
print(height)

#para 5 pessoas alterar tamanho do ciclo for