import random

numeroAleatorio = 0

for repeticion in range(10):
    print(repeticion)
    numeroAleatorio += random.randint(1,5)

print(numeroAleatorio)