numero_loteria ={13, 21, 22, 5, 8}

jugadores = [
    {"Nombre":"Federico", "Numero":{13, 21, 22, 5, 4}},
    {"Nombre": "Mariana", "Numero":{1, 2, 4, 21, 45, 5, 65}}

]

nombre_usuario = jugadores[0]["Nombre"]
numero_sorteo = jugadores[0]["Numero"].intersection(numero_loteria)

print(f"El jugador {nombre_usuario} acerto {len(numero_sorteo)} números.")

nombre_usuario_1 = jugadores[1]["Nombre"]
numero_sorteo_1 = jugadores[1]["Numero"].intersection(numero_loteria)

print(f"El jugador {nombre_usuario_1} acerto {len(numero_sorteo_1)} números.")




