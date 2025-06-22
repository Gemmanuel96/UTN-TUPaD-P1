#La búsqueda binaria es un algoritmo eficiente para encontrar un elemento dentro de una lista ordenada, donde funciona 
#Comparando el elemento que buscás con el del medio de la lista.

#Busqueda binaria

def busquedaBinaria(lista, num):
 
 
 inicio = time.time()   #Marcamos primero los parametros: Primer elemento y el ultimo de la lista
 primero = 0            #Primer elemento
 ultimo = len(lista)-1  #Ultimo elemento
 encontrado = False     #Usaremos como control lógico dentro del bucle while para saber si el número ya fue encontrado o no.
 posicion = -1          # Inicializamos por si no se encuentra
 
 while primero<=ultimo and not encontrado: 
    
    Medio = (primero + ultimo)//2   #Dividimos la lista a la mitad  
    
    if lista[Medio] == num:         #Si encuentra el elemento da True
        encontrado = True 
        posicion = Medio            # Guardamos la posición
    else:	
        if num < lista[Medio]:      #Cambia parametro: de la primera posicion hasta la mitad (de mitad a la izquierda)
           ultimo = Medio-1
        else:
            primero = Medio+1       #Cambia parametro: de la mitad de la lista hasta el final (de mitad hacia la derecha)
    
 final = time.time()
 duracion = final - inicio
 return encontrado, posicion, duracion # El elemento esta en la lista, la posicion de elemento y tiempo de ejecucion

#A tener en cuenta
#Para poder utilizar la busqueda binaria hay que tener la lista de elemento ordenada, ya sea de forma ascendente o descendente
#por que si la lista esta desordenada, no se podra utilizar la busqueda, por que la logica se bada en descartar mitades segun el orden


# El bubble sort optimizado mejora el algoritmo original al agregar una verificación en cada pasada. 
# Si durante una vuelta completa no se hacen intercambios, significa que la lista ya está ordenada y se detiene antes de tiempo. 
# Esto ahorra pasos innecesarios y mejora el rendimiento en listas que ya están parcialmente ordenadas.


#Ordenamiento Burbuja (creciente)
def ordenamientoBurbujaOptimo(lista):
    intercambios = True         #  Bandera que indica si hubo algún intercambio en la pasada
    pasada = len(lista) - 1      # Número de pasadas necesarias (comienza desde el final)

    while pasada > 0 and intercambios:  # Mientras queden pasadas y se hayan hecho intercambios

        inicio = time.time()
        intercambios = False             # Reinicio de la bandera en cada pasada
        
        for i in range(pasada):
            if lista[i] > lista[i + 1]:  # Si el elemento actual es mayor que el siguiente
                
                #Intercambio de valores
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                intercambios = True  # Hubo un intercambio, se debe seguir iterando

    
        pasada = pasada - 1  # Disminuimos la cantidad de elementos a comparar
    
    fin = time.time()
    tiempo = fin - inicio
    return lista, tiempo  #Devolvemos la lista ya ordenada y el tiempo

def ordenamientoBurbujaOptimodecreciente(lista):
    intercambios = True  # Bandera que indica si hubo algún intercambio en la pasad
    pasada = len(lista) - 1  # Número de pasadas necesarias (comienza desde el final)

    while pasada > 0 and intercambios:  # Mientras queden pasadas y se hayan hecho intercambios

        inicio = time.time()
        intercambios = False  # Reinicio de la bandera en cada pasada
        for i in range(pasada):
            if lista[i] < lista[i + 1]:  # Si el elemento actual es mayor que el siguiente
                #Intercambio de valores
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                intercambios = True  # Hubo un intercambio, se debe seguir iterando

    
        pasada = pasada - 1  # Disminuimos la cantidad de elementos a comparar
    
    fin = time.time()
    tiempo = fin - inicio
    return lista, tiempo  #Devolvemos la lista ya ordenada y el tiempo



import time #importamos la libreria de tiempo para calcular el tiempo de ejecucion de algoritmo
import random #Importamos random para numeros

#Listas

#200 Nombres
nombres = [
    "Norma", "Mario", "Lorenzo", "Melina", "Damian", "Andres", "Sebastian", "Rebeca", "David", "Virginia",
    "Gabriela", "Rocio", "Cintia", "Tatiana", "Erica", "Ulises", "Nahir", "Leonardo", "Wanda", "Thiago",
    "Delia", "Orlando", "Leonel", "Victor", "Daniel", "Tomas", "Gisela", "Mateo", "Bianca", "Soledad",
    "Yamila", "Fernando", "Candela", "Jacinta", "Yanina", "Hugo", "Natalia", "Malena", "Raul", "Margarita",
    "Graciela", "Luis", "Nazareno", "Pablo", "Claudio", "Cristian", "Julian", "Nora", "Agustina", "Celeste",
    "Zoe", "Celina", "Amalia", "Karen", "Ivan", "Nancy", "Simona", "Debora", "Facundo", "Guido",
    "Mariano", "Axel", "Irma", "Amparo", "Matias", "Ruben", "Emilia", "Ximena", "Diego", "Bruno",
    "Martina", "Zulma", "Sara", "Claudia", "Esteban", "Julio", "Javier", "Cecilia", "Joaquin", "Samuel",
    "Patricio", "Pilar", "Cristobal", "Roberto", "Miguel", "Cristina", "Tania", "Isabel", "Aldana", "Miranda",
    "Valeria", "Bautista", "Ariel", "Agustin", "Nelson", "Julieta", "Camila", "Jose", "Marcelo", "Jazmin",
    "Gonzalo", "Lorena", "Elisa", "Yolanda", "Nicanor", "Armando", "Teodoro", "Luciano", "Milagros", "Catalina",
    "Laura", "Ezequiel", "Sandra", "Marcela", "Carolina", "Felipe", "Veronica", "Mercedes", "Carlos", "Juan",
    "Eliana", "Noelia", "Raquel", "Salvador", "Renata", "Lara", "Pedro", "Angela", "Lautaro", "Vanesa",
    "Florencia", "Delfina", "Santiago", "Alan", "Hernan", "Beatriz", "Benjamin", "Emmanuel", "Magdalena", "Flor",
    "Nicolas", "Emilio", "Andrea", "Luisa", "Rodrigo", "Paola", "Marina", "Olga", "Alejandro", "Lucas",
    "Susana", "Francisco", "Tamara", "Ailen", "Valentin", "Martin", "Maia", "Ines", "Ernesto", "Victoria",
    "Sol", "Valentina", "Faustino", "Alma", "Karina", "Antonella","Juliana", "Juana", "Patricia", "Brenda", "Gustavo",
    "Nestor", "Silvia", "Ignacio", "Federico", "Maria", "Aixa", "Ricardo", "Mirta", "Vicente", "Gaston",
    "Guadalupe", "Anibal", "Franco", "Eugenia", "Estela", "Elsa", "Silvana", "Irene", "Lisandro", "Micaela",
    "Leandro", "Hector", "Romina", "Oscar", "Macarena", "Nadia", "Vilma", "Manuel", "Gabriel", "Josefina"]



numeros = list(range(0,200)) #Declaramos lista
random.shuffle(numeros) #Declaramos para desordenar la lista

print()
print("Mostramos como primer paso la listas desodenadas.")
print()
print("Lista de numeros = ")
print()
print(numeros)
jeje=input("") #Puntos de pausa
print("Lista de nombres = ")
print()
print(nombres)
print()

print("-----------------------------------------------------------------------------------------------------")
jeje= input("")

print("Aplicamos Orden Burbuja a las lista = ")

#Aplicamos la funcion
ordenamientoBurbujaOptimo(numeros)
ordenamientoBurbujaOptimo(nombres)

print("Lista de numeros Ordenadas: ")
print()
print(numeros)
jeje=input("")
print()
print("Lista de Nombres Ordenados:")
print()
print(nombres)


print("-----------------------------------------------------------------------------------------------------")
jeje=input("")
print("Aplicamos busqueda binaria: ")

#Numeros
num = int(input("Ingrese numero a buscar = "))
encontrado,posicion,duracion = busquedaBinaria(numeros,num)

if encontrado == False:
  print("El elemento no ese encuentra en la lista.")
else:
 print(f"Elemento = {numeros[posicion]}")
 print(f"Posicion = {posicion}")
 print(f"Tiempo de ejecucion = {duracion:.6}")



jeje = input("----------------------------------------------------------------------------------------------------------")
#Nombres
nom = input("Ingrese nombre a buscar = ")
encontrado,posicion,duracion = busquedaBinaria(nombres,nom)

if encontrado == False:
  print("El elemento no ese encuentra en la lista.")
else:
 print(f"Elemento = {nombres[posicion]}")
 print(f"Posicion = {posicion}")
 print(f"Tiempo de ejecucion = {duracion:.6}")

print("----------------------------------------------------------------------------------------------------------")
j= input()

print("Como ultima prueba, vamos hacer un ordenamiento decreciente, en donde vamos a ordenarlo de ultimo al primer posicion: ")

ordenamientoBurbujaOptimodecreciente(nombres)
ordenamientoBurbujaOptimodecreciente(numeros)

print("Lista de numeros decreciente:")
print(numeros)
j = input("----------------------------------------------------------------------------------------------------------")
print(f"Lista de nombres decreciente:")
print(nombres)
