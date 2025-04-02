edad=int(input("Ingrese su edad: "))

if (edad < 12):
    print("Sos un niño/a")

elif (edad >= 12  and edad < 18):
    print("Sos un adolecente")

elif(edad >=18 and edad < 30):
    print("Sos un Adulto/a joven")

elif (edad >= 30):
    print("Sos un adulto")
else:
    pass