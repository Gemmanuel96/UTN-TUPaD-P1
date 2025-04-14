num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = 0
cont = num
if num>=0 and num>0:
    while cont <= num2:
        suma += cont
        cont += 1
else:
    print("El segundo valor debe ser mayor que el primero")

print(f"La suma total es : {suma}")