#Funcion de potencia
def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m-1)
    
a= int(input("Ingrese un numero = "))
b= int(input("Ingrese potencia : "))

print(a,"^",b,"= ", potencia(a,b))