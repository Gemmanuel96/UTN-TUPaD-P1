#Cuenta regresiva
def cuenta_regresiva(x):

    import time
    if x == 0:
        print( "Despegue!")
    else:
        print(x)
        time.sleep(1)
        return cuenta_regresiva(x-1)

#Suma recursiva o factorial de un numero 
def factorial (x):
    if x == 0:
        return 0
    else:
        return x + factorial(x-1)


#Funcion fibonacci    
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion -1 ) + fibonacci_recursivo(posicion-2)