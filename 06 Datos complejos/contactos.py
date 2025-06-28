contactos = {}

print("Ingrese 5 contactos: ")
for i in range(0,5):
 nombre = input("Nombre = ")
 num = input("Numero de telefono : ")
 contactos[nombre] = num

print(contactos)


nom = input("Ingrese el nombre para saber el numero : ")

print(contactos[nom])