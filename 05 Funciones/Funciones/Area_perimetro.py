#Funciones
def calculo_area(num):
    area = 3.14 * (num**2)
    return area

def calculo_perimetro (num):
    perimetro = 2 * 3.14 * num
    return perimetro


#Programa principal
radio = int(input("Ingrese el Radio = "))
area = calculo_area(radio)
perimetro = calculo_perimetro(radio)

print(f"El area es {area}")
print(f"El perimetro es {perimetro}")