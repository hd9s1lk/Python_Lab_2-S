#Faça um algoritmo que leia o nome de uma pessoa na forma “nome de batismo” seguido 
#pelo seu “sobrenome” e imprima o nome na forma “sobrenome” seguido pelo “nome de 
#batismo”. 
#Exemplo: António José Mano - Mano, António José. 

first_name = input("Insira o seu primeiro nome: ")
last_name = input("Insira o seu último nome: ")

nome_total = first_name +" "+ last_name
batismo = last_name + " " +first_name

print("Nome Completo: " +nome_total)
print("Nome Batismo: " +batismo)