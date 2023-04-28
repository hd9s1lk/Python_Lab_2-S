# Considere uma equação do segundo grau 𝑓(𝑥) = 𝑎 · 𝑥2 + 𝑏 · 𝑥 + 𝑐. A partir dos coeficientes, 
#determine as raízes da equação. Dica: ∆ = 𝑏2 - 4 · 𝑎 · 𝑐: se delta é maior que 0, possui duas 
#raízes reais; se delta é 0, possui uma raiz; caso delta seja menor que 0, não possui raízes reais.

a = float(input("Insira um valor: \n"))
b = float(input("Insira um segundo valor: \n"))
c = float(input("Insira um terceiro valor: \n"))

delta = (b*b) - 4*a*c

if (delta>0):
    print("Possui duas raízes\n")
elif(delta==0):
    print("Possui uma raíz\n")
elif(delta<0):
    print("Não possui raízes\n")
else:
    print("Insira valores válidos:\n")