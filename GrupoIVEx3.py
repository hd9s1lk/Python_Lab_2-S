#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem 
#do distribuidor e dos impostos (aplicados sobre o custo de fábrica). Supondo que a 
#percentagem do distribuidor seja de 12% e os impostos de 45%, implemente um algoritmo 
#que leia o custo de fábrica do carro e imprima o custo ao consumidor final. 

ci = float(input("Insira o custo do carro: "))

perc_dis = ci * 0.12
taxes = ci * 0.45

final = float(ci + perc_dis + taxes)

print("Preço Final: %f " %(final))