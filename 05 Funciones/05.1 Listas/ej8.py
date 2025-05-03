doble = []
resultado = 0
num = 0

#Primer ciclo para ingreso de los valores
print("Ingrese los valores 5, 10 y 15: ")
for i in range (0,3):
    num = input("numero = ")
    doble.append(num)

#Ciclo para imprimir el doble
for i in range (0,3):
    numero = int(doble[i])
    resultado = numero * 2
    print(f"El doble de {numero} es = {resultado}")