#Implemente o exercício anterior fazendo com que o computador faça de jogador B. 

import random
x = random.randint(1,100)
b = 0


while(x != b):
    b = random.randint(1,100)

    if (x > b):
        print("O número é maior!")
        b = random.randint(b,100)
    if (x < b):
        print("O número é menor!")
        b = random.randint(1,b)
    if (x == b):
        print("Parabéns! Acertou no número!")
        print(x,b)
    