#Implemente um programa python que peça ao utilizador uma nota de avaliação, valor
#numérico de 0 a 20 (para este exercício não é necessário validar o valor introduzido), e
#que indique se o aluno está APROVADO (>=9.5) ou REPROVADO (<9.5). Atualize o código para
#contemplar, por exemplo: ORAL, para alunos com a nota superior a 16.


nota = float(input("Insira uma nota: \n"))

if (nota >= 9.5 and nota < 16):
    print("Aprovado")
if (nota <= 9.5):
    print("Reprovado")
if (nota >= 16):
    print("Vais a Oral!")
