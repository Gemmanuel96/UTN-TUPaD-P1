lista = list(range(1,101))

print("Los numeros multiplos de 4 : ")
for i in range (1,100):
    lista2 = lista[i] ## Guardamos la posicion de i

    ##Luego verificamos el valor dentro de la lista valor "i"
    if lista2 % 4 == 0:
        print (lista2, end=" ")