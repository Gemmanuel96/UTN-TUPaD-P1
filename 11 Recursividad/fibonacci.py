#Declaramos la funcion de fibonacci
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion -1 ) + fibonacci_recursivo(posicion-2)

num = int(input("Ingrese un numero de posicion = "))

print("Posicion ",num, "= ",fibonacci_recursivo(num))
print()
print("Mostramos lista de fibonacci ")

#Iniciamos un for para mostrar las posiciones de 0 hasta el numero ingresado
for i in range (0, num +1): 
    print(i,"= ",fibonacci_recursivo(i))