#Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o utilizador
#digite um número fora desse intervalo, deverá aparecer uma mensagem informando
#que não existe o mês com este número.


num = int(input("Insira um valor inteiro: \n"))

if(num == 1):
    print("Janeiro\n")
if(num == 2):
    print("Fevereiro\n")
if(num == 3):
    print("Março\n")
if(num == 4):
    print("Abril\n")
if(num == 5):
    print("Maio\n")
if(num == 6):
    print("Junho\n")
if(num == 7):
    print("Julho\n")
if(num == 8):
    print("Agosto\n")
if(num == 9):
    print("Setembro\n")
if(num == 10):
    print("Outubro\n")
if(num == 11):
    print("Novembro\n")
if(num == 12):
    print("Dezembro\n")
elif(num > 12 and num <= 0):
    print("Insira valores válidos\n")
    