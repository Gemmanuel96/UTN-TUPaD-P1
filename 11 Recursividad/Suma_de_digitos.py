def contar_bloques (numero):
    if numero == 0 :
        return 0
    else:
        return numero + contar_bloques(numero-1)
    
numero = int(input("Ingrese la numero de bloques de la base = "))
print("Bloques totales = ",contar_bloques(numero))