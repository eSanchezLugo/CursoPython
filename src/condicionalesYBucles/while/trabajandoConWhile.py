contador = 0 

while contador <10 :
    print("Hola")
    contador = contador + 1
print("Hemos salido del bucle")


edad = int(input("Ingresa tu edad, por favor : "))

while edad <0 or edad> 100:
    print(" Haz introducido una edad no valida")
    edad = int(input("Ingresa tu edad, por favor : "))

print("Gracias puedes pasar")
print("Edad del usuario : " + str(edad))
    
