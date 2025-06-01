def agregar_elemento_lista (lista,elemento): ##Agregar Elementos
     lista.append(elemento)

suma = 0
lista = []
num = int(input("Ingrese elemento hasta que ingrese 0 = "))

def Agregar_numeros(lista,num):
  while num>0:
    agregar_elemento_lista(lista,num)
    num = int(input())
