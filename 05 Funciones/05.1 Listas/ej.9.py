#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
import time
compra=""
#Primer paso, mostramos la lista inicial
compra = [["Pan", "Leche"], ["Arroz", "Fideos", "Salsa"], ["Agua"]]
print("Esta es la lista inicial :")
print(compra)
print("------------------------------------------")
time.sleep(1)

#Agregar elemento a lista 3
print("1)Agregar jugo al 3 cliente = ")
compra_2 = input("Ingrese compra = ") 
compra[2].append (compra_2) #Agregamos con append
print("Lista nueva : ")
print(compra)
print("--------------------------------------------------")
time.sleep(1)

#Reemplazamos fideos por tallarines
print("2)Reemplazamos fideos por tallarines:")
compra[1][1] = "Tallarines" #Cambiamos con slicing
print(f"Lista = {compra}") 
print("---------------------------------------------------")
time.sleep(1)

#Eliminamos pan
print("3)Eliminamos 'pan' del primer cliente :")
compra[0].remove("Pan") #Eliminamos 'pan' 
print("Lista :",compra)
print("----------------------------------------------------")

time.sleep(1)
print("Lista final = ",compra)