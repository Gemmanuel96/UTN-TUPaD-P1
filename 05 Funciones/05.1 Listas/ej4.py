import time #Funcion tiempo

print("Valor de la lista: ")
lista = ["perro", "gato","conejo","pez"]
print(lista) #Imprimimos primeros elementos de la lista
print()
time.sleep(1)

print("Cambiamos de lista el segundo y el ultimo por loro y oso: ")
lista[-3]="loro" #Indexin con numeros negativos
lista[-1]="oso"

print(lista)