def promedio_3(a,b,c):
    prom = (a+b+c) / 3
    return prom


print("Ingrese 3 notas para calcular el promedio = ")
a=int(input())
b=int(input())
c=int(input())
promedio = promedio_3(a,b,c)

print(f"El promedio final es  = {round(promedio,2)}")