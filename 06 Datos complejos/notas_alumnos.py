print("Ingrese el nombres de 3 alumnos: ")

alumnos ={} #diciconario alumnos


for i in range(0,3):
    nom = input("Alumno = ")
    
    notas = [] #notas como lista

    for j in range(0,3):
        nota = int(input("Ingrese nota = "))
    notas.append(nota)

    alumnos [nom] = tuple(notas) #Le asignamos las notas tupla al diccionario


#Itineramos item por item y calculamos el promedio
for nombre,notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} = {promedio}")