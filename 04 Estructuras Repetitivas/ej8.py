print("Ingrese 100 numero y se deteminara si son: positivos,negativos,pares o impares.")
par = 0
impar = 0
negativo = 0
positivo = 0 
cero = 0

for i in range(1,101):
    
    num=int(input(f"Numero {i}: "))
    
    ##Verificamos si el numero ingresado es par o impar
    if num == 0:
        cero += 1
    elif num % 2 == 0:
        par += 1
    else:
        impar +=1

    ##Verificamos si el numero es Positivo, nagetivo, o igual a cero
    if num>0:
        positivo += 1
    elif num<0:
        negativo += 1
  

print(f"Positivos = {positivo}")
print(f"Negativos = {negativo}")
print(f"Pares = {par}")
print(f"Impares = {impar}")
print(f"Iguales a cero = {cero}")