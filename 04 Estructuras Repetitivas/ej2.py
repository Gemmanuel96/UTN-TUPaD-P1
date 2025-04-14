num = int(input("Ingrese un numero entero : "))
cont = 0
if num == 0:
    cont = 1
    print("Solo tiene un solo digito")
else:
    while num > 0:
        num = num // 10
        cont = cont + 1

print("El numero de digitos es : "+ str(cont))