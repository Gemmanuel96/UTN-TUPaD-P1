palabra = input("Ingrese una frase o una palabra : ")

if palabra.lower().endswith (("a","e","i","o","u")):
    print(palabra +"!")
else:
    print(palabra)