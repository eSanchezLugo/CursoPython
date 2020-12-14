import random

numeroAleatorio = random.randint(1,100)

numero = int(input("Introduce un número entre 1 y 100 , por favor : "))

intentos= 1

while numero != numeroAleatorio:
    if numero>numeroAleatorio:
        print("El número aleatorio es menor al introducido")  
    if numero < numeroAleatorio:
        print("El número aleatorio es mayor al introducido ")

    numero = int(input("Introduce un número entre 1 y 100 , por favor : "))

    intentos = intentos +1
    if intentos == 20:
        break

if intentos == 20:
    print("Sigue intentando adivinar el numero aleatorio")
else :
    print("Logrado, has realizado " + str(intentos) + " intentos")  


    