#Funciones
def tabla_de_multiplicar(num):
    resultado = 0
    for i in range (1,11):
        resultado = i * num
        print(f"{num} X {i} = {resultado}")
    

print("Tabla de Multiplicar")

num = int(input("Ingrese un numero : "))
tabla = tabla_de_multiplicar(num)