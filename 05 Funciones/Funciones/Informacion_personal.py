#Funciones
def informacion_personal (mensaje):
    print(mensaje)
    nombre = input("Nombre = ")
    apellido = input("Apellido = ")
    edad = input("Edad = ")
    residencia = input("Residencia = ")
    return (nombre,apellido,edad,residencia) #Se hizo una tupla

datos = (informacion_personal("Ingrese su datos personales : "))

print(f"Hola {datos[0]} {datos[1]}, tenes {datos[2]} años y vivis en {datos[3]}.")