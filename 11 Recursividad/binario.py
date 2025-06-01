def binario(num):
    if num == 0:  # Punto base, para cuando llegue a 0 no muestre nada
        return ""    
    else:      #Division entera    #Resto es binario
        return binario(num // 2) + str (num%2) 
    
numero = int(input("Ingrese un numero = "))

print(numero, "= ", binario(numero) )
