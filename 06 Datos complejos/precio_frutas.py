#Diccionario de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

#Agregamos mas frutas
precios_frutas['Naranjas'] = 1200
precios_frutas['Manzanas'] = 1500
precios_frutas['Pera'] = 2300

#Mostramos el resultado
print(precios_frutas)

precios_frutas['Manzanas'] = 1700
precios_frutas['Banana'] = 1330
precios_frutas['Melón'] = 2800

print(precios_frutas)
frutas = list(precios_frutas.keys())

print(frutas)