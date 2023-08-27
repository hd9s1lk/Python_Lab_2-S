#Considere o seguinte jogo entre dois jogadores: O jogador A pensa num número entre 1 
#e 100. O jogador B tem n tentativas para descobrir esse número. Em cada tentativa o 
#jogador A deve dizer se o número que o jogador B disse é o correto ou se é maior ou 
#menor do que o número pensado. Escreva um programa que implemente este jogo sendo 
#o computador o jogador A. 
import random
x = random.randint(1,100)
b = 0


while(x != b):
    b = int(input("Tente adivinhar o número de 1 a 100: "))

    if (x > b):
        print("O número é maior!")
    if (x < b):
        print("O número é menor!")
    if (x == b):
        print("Parabéns! Acertou no número!")
    