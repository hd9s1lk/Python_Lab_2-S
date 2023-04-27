#Implemente um programa python que converta um par de valores hora, minutos no
#formato 24 horas para o formato AM/PM.
#Exemplo: 13:07  1:07 PM ou 00:07 12:07AM

op=int(input("Escreva 1 para 24->12 ou 2 para 12->24"))

if 0<op <=2:
    if op==1:
        hora=input("Introduza as horas em formato 24 horas (hh:mm)").split(':')

        if int(hora[0]) > 12:
            hora[0]=str(int(hora[0])-12)
            print("São",hora,"PM")
        else:
            print("São",hora,"AM")
    if op==2:
        hora=input("Introduza as horas em formato (hh:mm AM/PM)").replace(':','').split('')

        if hora[2].upper()=='AM':
            print("São",hora,"Em formato 24 horas")
        elif hora[2].upper()=='PM':
            a=int(hora[0])
            a+=12
            if a>24:
                a-=24
                hora[0]=str(a)
                print("São",hora,"Em formato 24 horas")
            else:
                print("Valor inválido")