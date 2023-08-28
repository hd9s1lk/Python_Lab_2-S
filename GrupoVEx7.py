#Faça um programa que peça quatro notas de 10 alunos, calcule e armazene num vetor a 
#média de cada aluno e imprima o número de alunos com média maior ou igual a 7,0.

aluno1 = []
aluno2 = []
medias = []
i=0

for nota in range(0,4):
    var1 = float(input("Insere aqui as tuas notas: "))
    aluno1.append(var1)

print(aluno1)
media1 = sum(aluno1) / len(aluno1)
medias.append(media1)
print(medias)

for nota in range(0,4):
    var2 = float(input("Insere aqui as tuas notas: "))
    aluno2.append(var2)

print(aluno2)
media2 = sum(aluno2) / len(aluno2)
medias.append(media2)
print(medias)

for media in medias:
    if media >= 7.0:
        i+=1
    else:
        continue

print(i)

#PARA SER DE 10 ALUNOS PARA CRIAR MAIS LISTAS E CICLOS




