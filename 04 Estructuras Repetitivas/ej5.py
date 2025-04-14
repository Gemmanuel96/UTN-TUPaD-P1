import random

numero_secreto= random.randint(0,9)
intentos = 1

print("Adivine el numero secreto! ")
print("")
num = int(input(f"Ingrese un numero, intento {intentos} :"))

if num == numero_secreto : # Hacemos un if por si de adivina el numero al primer intento
    print(f"Felicidades ha adivinado el numero secreto {numero_secreto}!, en {intentos} intento")

else:   # sino entramos la segunda opcion, donde se entrara al bucle para seguir intentando

    while num != numero_secreto:
        intentos = intentos + 1 
        num = int(input(f"Ingrese otro numero, intento {intentos} :"))
    
    print(f"Felicidades ha adivinado el numero secreto {numero_secreto} en {intentos} intentos! ")