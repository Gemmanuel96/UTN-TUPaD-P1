def analizar_dni(dni):
    digitos = list(str(dni))
    conjunto = set(digitos)
    suma = sum(int(d) for d in digitos)
    frecuencia = {d: digitos.count(d) for d in conjunto}
    return conjunto, suma, frecuencia