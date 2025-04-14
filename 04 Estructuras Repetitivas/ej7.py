numero = int(input("Ingrese un numero entero :"))
suma = 0
cont = 0

if numero == 0: ## Si el numero ingresado es igual a 0
    print(f"La suma total = {suma} ")
elif numero>0:
    while (cont <= numero): ## Se sumara se 0 hasta el numero que indico el usuario
        suma = suma+ cont
        cont=cont + 1
    print(f"La suma total es : {suma}")
elif numero<0:
    print("El numero debe de ser positivo")