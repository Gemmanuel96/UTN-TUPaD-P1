contraseña = input("Ingrese contraseña:")

resultado = len(contraseña)

#Inicio de IF

if (resultado>= 8 and resultado<=14):
    print("Ha ingresado contraseña correctamente")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Finalizacion de if