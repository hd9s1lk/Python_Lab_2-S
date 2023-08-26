# Elabore um programa python que simule uma aplicação que registe a pescaria de um 
#barco de pesca. O barco, nos seus porões, pode carregar, no máximo, 150 Toneladas. A 
#cada pescaria deve ser registado o valor pescado e somado ao pescado anteriormente. 
#Quando atingir ou ultrapassar o valor máximo, a aplicação de terminar e o utilizador deve 
#ser informado se tem, ou não, de deitar peixe ao mar e, em caso afirmativo, que 
#quantidade.

pescado = float(input("Insira as toneladas de peixe pescado: "))

if pescado > 150:
    fora = pescado - 150
    print("Terá que deitar fora %f" %(fora))
elif pescado == 150:
    print("Atingiu a capacidade máxima de peixe!")
elif pescado < 150:
    resto = 150 -pescado
    print("Poderá ainda pescar %f" %(resto))
else:
    print("Insira um valor válido!")
