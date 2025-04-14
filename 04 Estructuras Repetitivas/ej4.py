num = int(input("Ingrese numeros enteros (0 para terminar) :"))
suma = 0

while num != 0:
    suma = suma + num
    num=int(input("Ingrese otro numero (0 para terminar):"))

print(f"La suma total es : {suma}")