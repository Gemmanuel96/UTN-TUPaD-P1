emisferio = input("Ingrese Emiferio: ")
dia = int(input("Ingrese fecha: "))
mes = int(input("Ingrese mes : "))

##Emisferio Sur
if (emisferio == "Sur" or emisferio == "sur"):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia<=20):
        print("Verano") 
    
    elif (mes == 3 and dia >= 21) or (mes == 4) or(mes == 5) or (mes==6 and dia <=20):
        print("Otoño")

    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
        print("invierno")
    
    elif (mes == 9 and dia >=21) or(mes == 10) or(mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    
    else:
        print("Fecha no valida.")


##Emisferio Norte
if (emisferio == "Norte" or emisferio == "norte"):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia<=20):
        print("Invierno") 
    
    elif (mes == 3 and dia >= 21) or (mes == 4) or(mes == 5) or (mes==6 and dia <=20):
        print("Primavera")

    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
        print("Verano")
    
    elif (mes == 9 and dia >=21) or(mes == 10) or(mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    
    else:
        print("Fecha no valida.")