def indice_imc(p,a):
    imc = p / (a**2)
    return imc



peso = float(input("Ingrese peso = "))
altura = float(input("Ingrese altura = "))

imc = indice_imc(peso,altura) 

print("Tu indice de masa corporal es = ",(round(imc,2)))