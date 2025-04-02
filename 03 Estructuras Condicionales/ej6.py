from statistics import mode, median, mean
import random

numeros_Aleatorios = [random.randint(1,100) for i in range (50)]

media = mean(numeros_Aleatorios)
mediana = median(numeros_Aleatorios)
moda = mode(numeros_Aleatorios)

print(f"Media = {media}")
print(f"Mediana = {mediana}")
print(f"Moda = {moda}")

if( media > mediana and mediana > moda ):
    print("Sesgo positivo o a la derecha")

elif (media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")

elif (media == mediana and mediana == moda):
    print("Sin sesgo")

else :
    print("No hay ningun sesgo claro")