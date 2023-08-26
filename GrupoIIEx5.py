#No dia da estreia do filme "À procura de Dory", uma grande emissora de TV realizou uma pesquisa logo 
# após o encerramento do filme. Cada espectador respondeu a um questionário no qual constava a sua idade e a sua opinião em relação ao filme: 
# excelente - 3; bom - 2; regular - 1. Crie um programa que receba a idade e a opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam “excelente”;
#• A quantidade de pessoas que responderam “regular”;
#• A percentagem de pessoas que responderam “bom”, de entre todos os espectadores analisados.

i=1

while(i!=5):
    

    idade = int(input("Insira a sua idade: \n"))
    grade = int(input("O que achou do filme? 3-Excelente, 2-Bom, 1-Regular\n"))
    
    cont=0
    perc=0
    idadeF=0
    
    if(grade==3):
        idadeF = idadeF + idade
        
    if(grade==2):
        cont +=1  
    if(grade==1):
        perc +=1
    

    media = idadeF / 5
    print(media)

    print(cont)

    percF = (perc/5) *100
    print(percF)

    i=+1


