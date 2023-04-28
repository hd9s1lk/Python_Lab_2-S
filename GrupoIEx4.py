#Implemente um programa em python que converta um valor em bytes para um formato
#humanamente legível (Kilo, Mega, Giga ou Tera bytes consoante o múltiplo que melhor se
#adapte a uma representação de fácil leitura do valor). Considere 1KBytes = 1024 Bytes.
#Exemplo: 16548973 bytes = 15,78 MBytes.

unit = int(input("Insira um numero de bits: \n"))


if (unit >= 1 and unit <8):
    print("%d bits" %(unit))
if (unit == 8):
    print("1 Byte")
if (unit >8 and unit <1024):
    print("%d Bytes" %(unit))
if (unit == 1024):
    print("1 KBytes\n") 
if (unit > 1024 and unit < 1048576):
    kb = unit * 0.000125
    print("%f KBytes" %(kb))
if(unit== 1048576):
    print("1 MegaBytes\n")
if(unit > 1048576 and unit < 1073741824):
    mb = unit * 0.0001192
    print("%f MegaBytes\n" %(mb))
if(unit == 1073741824):
    print("1 Gigabyte\n")


