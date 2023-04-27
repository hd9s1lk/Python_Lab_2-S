#Elabore um programa python que permita calcular a média de um aluno atendendo às
#notas obtidas em dois testes. O programa deve apresentar se o aluno foi aprovado ou
#reprovado, tendo em conta que um aluno aprova sempre que a média é superior ou
#igual a 10 valores.

nota1 = float(input("Insira a primeira nota: \n"))
nota2 = float(input("Insira a segunda nota: \n"))

media = (nota1+nota2) / 2

if(media >= 9.5):
    print("Aprovado com %f" %(media))
if(media < 9.5):
    print("Reprovado com %f" %(media))
else:
    print("Insira valores válidos")