#Funciones
def celcius_a_fahrenheit(num):
    f = (num * 9/5 ) + 32
    return f

#Programa Inicial
num =int(input ("Ingrese la temperatura en C° = "))
temperatura = celcius_a_fahrenheit(num)
print(f"La temperatura en de C° a Fahrenheit es = {temperatura}")

