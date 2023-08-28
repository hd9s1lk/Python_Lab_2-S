#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são: 
#a. "Telefonou à vítima?" 
#b. "Esteve no local do crime?" 
#c. "Mora perto da vítima?" 
#d. "Devia dinheiro à vítima?" 
#e. "Já trabalhou com a vítima?" 
#O programa deve, no fim, emitir uma classificação sobre a participação da pessoa no 
#crime. Se a pessoa responder positivamente a 2 questões deve ser classificada como 
#"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será 
#classificado como "Inocente".

bystander1 = []
#bystander2 = []
#bystander3 = []
#bystander4 = []
#bystander5 = []
#bystander6 = []



for question in range(0,1):
    var = input("Telefonou à vítima? (sim/não)\n")
    if var == "sim":
        bystander1.append(1)
    else:
        bystander1.append(0)
    var2 = input("Esteve no local do crime? (sim/não)\n")
    if var2 == "sim":
        bystander1.append(1)
    else:
        bystander1.append(0)
    var3 = input("Mora perto da vítima? (sim/não)\n")
    if var3 == "sim":
        bystander1.append(1)
    else:
        bystander1.append(0)
    var4 = input("Devia dinheiro à vítima? (sim/não)\n")
    if var4 == "sim":
        bystander1.append(1)
    else:
        bystander1.append(0)
    var5 = input("Já trabalhou com a vítima? (sim/não)\n")
    if var5 == "sim":
        bystander1.append(1)
    else:
        bystander1.append(0)

soma = sum(bystander1)

if soma == 2:
    print("Suspeita")
if soma == 3 or soma == 4:
    print("Cúmplice")
if soma == 5:
    print("Assassino")
else:
    print("Inocente")

#para os restantes é só adicionar ciclos
    
    
