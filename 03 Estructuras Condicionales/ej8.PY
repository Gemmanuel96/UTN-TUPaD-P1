nombre = input("Ingrese su nombre: ")

print("1)Si quiere su nombre en mayuscula. ")
print("2)Si quiere su nombre en minuscula.")
print("3)Si quiere su nombre con la primera letra Mayuscula.")

opcion=int(input("Opcion :"))

if opcion == 1 :
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3 :
    print(nombre.title())
else:
    print("Opcion no valida")