import time

horaActual = time.localtime().tm_hour
print(horaActual)

if horaActual >= 19:
    print("Es hora de ir a casa")
else:
    horaFinal = 19
    minutosRestantes = 60 - time.localtime().tm_min
    segundosRestantes = 60 - time.localtime().tm_sec
    segundosTotales = minutosRestantes * 60 + segundosRestantes
    tiempoRestante = time.strftime("%H:%M:%S", time.gmtime(segundosTotales))
    print(f"Todavía quedan {tiempoRestante} de trabajo")