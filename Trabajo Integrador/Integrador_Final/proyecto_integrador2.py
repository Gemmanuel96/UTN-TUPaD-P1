#Este tipo de ordenamiento
def ordenamientoBurbuja(lista):
    inicio = time.time()            #Iniciamos el timepo
    for pasadas in range(len(lista)-1,0,-1): #iniciamos el ciclo para el ordenamiento
        
        for i in range(pasadas): #Ciclo de comparacion
            if lista[i]>lista[i+1]:  #hacemos comparacion de primer elemento con el siguiente elemento si: i es mayor que i+1 hace el intercambio de ordenada
                temp = lista[i]      #si es guardamos el primer elemento en vaariable temporal
                lista[i] = lista[i+1] #guardamos el segundo elemento en la primera posicion
                lista[i+1] = temp     #guardamos el elemento que estaba en variable temp, en i+1, y se hace el intercambio de ordenada

    fin = time.time() 

    tiempo = fin - inicio #Calculamos el tiempo de ordenamien
    return tiempo


#Busqueda secuencial
def busquedaSecuencial(lista,n):
 inicio = time.time() ## Inicio de tiempo
 
 posicion = 0
 encontrado = False 
 
 while posicion < len(lista) and not encontrado: ##la funcion len nos permite itinerar hasta el ultimo elemento de la lista
  if lista[posicion] == n:
   encontrado = True
  else:
   posicion +=1

   
 fin = time.time()
 duracion = fin - inicio  ##Finalizacion de tiempo de ejecucion
 return encontrado, duracion, posicion #Hacemos una tupla para poder guardar las variables


import random
import time
#Listas

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

numeros = list(range(0,200))
random.shuffle(numeros) #Desordena elementos de la lsita de numero





print("")
print("Mostramos Busqueda secuencial, con elementos desordenados: ")
#busqueda secuencial Elementos desordenados
nom = input("Ingrese un nombre : ")

encontrado, tiempo, posicion = busquedaSecuencial(nombres,nom)

if encontrado == False:
   print("El nombre no esta en la lista.")
   print(f"Tiempo de busqueda : {tiempo:.6}")
else:
   print(f"Elemento = {nombres[posicion]}")
   print(f"Posicion = {posicion}")
   print(f"Tiempo = {tiempo:.6}")

print("----------------------------------------")

num = int(input("Ingrese un numero : "))

encontrado, tiempo, posicion = busquedaSecuencial(numeros,num)

if encontrado == False:
   print("El nombre no esta en la lista.")
   print(f"Tiempo de busqueda : {tiempo:.6}")
else:
   print(f"Elemento = {numeros[posicion]}")
   print(f"Posicion = {posicion}")
   print(f"Tiempo = {tiempo:.6}")

jeje = input()
jeje = input("Aplicamos ordenamiento Burbuja a ambas Listas: ")

#Ordenamiento burbuja clasica
tiempo = ordenamientoBurbuja(numeros)

print(f"Lista de numeros Ordenados = {numeros}")
jeje = input()
print(f"Tiempo de ordenamiento = {tiempo:.6}")
jeje = input()

tiempo = ordenamientoBurbuja(nombres)
print(f"Lista de nombres Ordenados : {nombres}")
jeje = input()
print(f"Tiempo de Ordenamiento = {tiempo:.6}")

print("--------------------------------------------------------")
print("")

print("Mostramos Busqueda secuencial, con elementos ordenados: ")

nom = input("Ingrese un nombre : ")

encontrado, tiempo, posicion = busquedaSecuencial(nombres,nom)

if encontrado == False:
   print("El nombre no esta en la lista.")
   print(f"Tiempo de busqueda : {tiempo:.6}")
else:
   print(f"Elemento = {nombres[posicion]}")
   print(f"Posicion = {posicion}")
   print(f"Tiempo = {tiempo:.6}")

print("----------------------------------------")

num = int(input("Ingrese un numero : "))

encontrado, tiempo, posicion = busquedaSecuencial(numeros,num)

if encontrado == False:
   print("El nombre no esta en la lista.")
   print(f"Tiempo de busqueda : {tiempo:.6}")
else:
   print(f"Elemento = {numeros[posicion]}")
   print(f"Posicion = {posicion}")
   print(f"Tiempo = {tiempo:.6}")

