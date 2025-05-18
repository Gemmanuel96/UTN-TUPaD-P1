def operaciones_f(a,b):
    suma = a+b
    resta = a-b
    multiplicacion= a*b
    division = a // b if b!=0 else "No se puede dividir por cero "
    return (suma,resta,multiplicacion,division) #tupla (0,1,2,3) (tienen posiciones)


print("Ingrese 2 numero: ")
num = int(input())
num2= int(input())

resultado = operaciones_f(num,num2)

print(f"Suma= {resultado[0]}")
print(f"Resta= {resultado[1]}")
print(f"Multiplicacion= {resultado[2]}")
print(f"Divicion = {resultado[3]}")
