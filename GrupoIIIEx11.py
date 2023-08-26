#Elaborar um programa python que leia as notas de uma turma de, no máximo, 60 alunos 
#num exame de uma disciplina e calcule a sua média. O professor deve apenas inserir as 
#notas dos alunos que fizeram o exame, não sendo imperativo que haja a inserção das 60 
#notas visto que podem existir alunos que tenham faltado ao exame

i=0
nota = []
total = 0

while(i!=3):
    a = input("Tiveste presente no exame?: ")
    if (a == "sim"):
        num = float(input("Insere a tua nota:"))
        nota.append(num)
        total = sum(nota)
        i+=1
    else:
        print("Passa para o próximo rei!")
        i+=1

media = float(total/len(nota))

print("Média dos testes: %f" %(media))