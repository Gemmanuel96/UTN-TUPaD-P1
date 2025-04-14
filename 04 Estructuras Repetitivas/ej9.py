suma = 0
cantidad = 100

print("Ingrese 100 numeros enteros: ")

for i in range (1,cantidad +1):
    num= int(input(f"Ingrese valores {i} : "))
    suma = suma + num

promedio = suma / cantidad #Calculamos la medio de los numeros ingresados

print(f"El promedio es : {promedio}") 