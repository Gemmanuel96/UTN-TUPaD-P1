magnitud = float(input("Ingrese magnitud de terremoto :"))

if magnitud < 3 :
    print("Muy leve (Imperceptible).")

elif magnitud>=3 and magnitud<4 :
    print("Leve (ligeramente perceptible.)")

elif magnitud>=4 and magnitud < 5:
    print("Moderado (sentido por personas,pero generalmente no causa daños.)")

elif magnitud>= 5 and magnitud<6:
    print("Fuerte (puede causar daños significativos.)")

else:
    print("Extremo (puede causar daños a gran escala.)")