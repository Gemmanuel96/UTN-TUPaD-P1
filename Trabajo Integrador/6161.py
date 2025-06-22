def ingreso_de_dni (lista,cantidad,mensaje):
    for i in range(0,cantidad+1):
        elemento = (input(mensaje))
        elemento = set(map(int, elemento))
        lista.append(elemento)

lista = []

num = int(input("Ingrese cunatos elementos va a ingresar = "))
ingreso_de_dni(lista,num,"Ingrese elemento = ")

print(lista[0])