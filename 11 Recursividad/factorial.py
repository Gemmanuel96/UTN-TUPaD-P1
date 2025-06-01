##Funcion factorial, con recursividad
def factorial (x): 
    if x == 0:
        return 0
    else:
        return x + factorial(x-1)
    
    
num = int(input("Ingrese un numero = ")) ## Ingresamos un numero

#Entramos en el ciclo para que vaya desde 1 hasta el numero indicado,
#Como siguiente paso, nos mostrara el factorial de todos los numeros desde 1 hasta el numero indicado

for i in range( 1, num+1): 
     print(i,"=" , factorial(i)) #Nos muestra en pantalla el factirial de dicho numero