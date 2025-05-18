def segundos_a_hora(segundos):
    hora = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return (hora,minutos,segundos) #Esto es una tupla, es como una lista pero no se puede modificar-. ()

segundos = int(input("Ingrese segundos:"))
horas = segundos_a_hora(segundos)

print(f"El tiempo final {horas[0]}hr, {horas[1]} min, {horas[2]} seg.")

