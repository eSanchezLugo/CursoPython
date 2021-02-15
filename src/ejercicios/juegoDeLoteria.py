import random

numero_loteria = set(random.sample(range(22), 6))

jugadores = [
    {'nombre': 'Rolf', 'numeros': {1, 3, 5, 7, 9, 11}},
    {'nombre': 'Charlie', 'numeros': {2, 7, 9, 22, 10, 5}},
    {'nombre': 'Anna', 'numeros': {13, 14, 15, 16, 17, 18}},
    {'nombre': 'Jen', 'numeros': {19, 20, 12, 7, 3, 5}}
]


numero_jugador = jugadores[0]

for jugador in jugadores :
    numeros_coincidencia = len(jugador["numeros"].intersection(numero_loteria))
    if numeros_coincidencia > len(numero_jugador["numeros"].intersection(numero_loteria)):
        numero_jugador = jugador

monto_ganado = 100 ** len(numero_jugador["numeros"].intersection(numero_loteria))

print(f"{numero_jugador['nombre']} gano {monto_ganado}.")