#Elabore um programa python que faça a classificação qualitativa de uma nota de um aluno 
#segundo os seguintes níveis: [0,5[ = péssimo; [5,8[ = mau; [8,10[ = insuficiente;
#[10,12[ = suficiente; [12,16[ = bom; [16,20] = excelente. Valide o valor introduzido.

nota = float(input("Insira uma nota: \n"))

if(nota >= 0 and nota < 5):
    print("Péssimo\n")
elif(nota >= 5 and nota < 8):
    print("Mau\n")
elif(nota >= 8 and nota < 10):
    print("Insuficiente\n")
elif(nota >= 10 and nota < 12):
    print("Suficiente\n")
elif(nota >= 12 and nota < 16):
    print("Bom\n")
elif(nota >= 16 and nota <= 20):
    print("Exclente\n")
else:
    print("Insira valores válidos \n")



