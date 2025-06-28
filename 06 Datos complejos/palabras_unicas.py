#pedimos una frase
frase = input("Ingrese una frase o palabras : ")

#Separamos la frase en elementos
palabras = frase.split()


#Separamos los elementos en elemetos unicos
palabras_unicas = set(palabras)

#creamos diccionario
recuento = {}

#itineramos palabra por palabra
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras unicas = ", palabras_unicas)
print("Diccionario = ", recuento)