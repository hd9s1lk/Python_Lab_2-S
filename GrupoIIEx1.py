#Elabore um programa em que o utilizador digite um número à sua escolha e seja impressa a respetiva tabuada.
#Ex:
#Digite um nº: 3
#3 x 1 = 3
#3 x 2 = 6
#…
#3 x 9 = 27
#3 x 10 =30

a = int(input("Insira um numero: \n"))

for i in range(11):
    result = a * i
    print(result)