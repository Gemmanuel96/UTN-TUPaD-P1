autos = ["Sedan","polo","suran","gol"]
print(f"Los valores de lista = {autos}")


print("Ingrese 2 valores nuevos : ")
n_autos =""
for i in (1,2): #Para poder ingresar elemnto 1 y 2
    n_autos= input("Ingrese palabra = ") 
    autos[i] = n_autos

#Imprimimos en pantalla la nuyeva lista
print(f"Nueva lista = {autos}") 