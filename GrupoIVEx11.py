#Vamos supor que nos são atribuídos 100€ para fazer apostas num jogo. O jogo consiste 
#no seguinte: de cada vez que se fizer uma jogada, o programa gera aleatoriamente um 
#valor que pode ser 0 ou 1. Se o valor obtido for zero o jogador perde o que apostar, se for 
#1 ganha um valor igual ao da sua aposta. O programa deve perguntar quanto queremos 
#apostar e fazê-lo dentro de um ciclo que dure enquanto o número de jogadas não 
#ultrapassar 10 e/ou enquanto tivermos dinheiro. Não podem ser aceites apostas 
#superiores ao dinheiro disponível em cada momento.
import random

cash = 100
jogadas = 0



while(cash > 0 and jogadas <10):
    aposta = int(input("Quanto quer apostar: "))

    if(aposta > cash):
        print("Você não possui essa quantia de dinheiro!\n")
        break
        
    x = random.randint(0,1)

    guess = input("0 ou 1?\n")

    if (guess == x):
            print("Era o preço da montra! Parabéns! Ganhou %d" %(aposta))
            cash += aposta
            print("Sua carteira: %d" %(cash))
    if (guess != x):
            print("Erraste nininho! Perdeste %d" %(aposta))
            cash -= aposta
            print("Sua carteira: %d" %(cash))
    if (cash == 0):
            print("Game Over!")
            exit()
    jogadas+=1

