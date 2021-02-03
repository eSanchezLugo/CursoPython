amigos = ["Andrea", "Fabian", "Felix", "Monica"]
familia = ["Roxana", "Aurelio", "Diana", "Jesus", "Rubí"]

nombre_usuario = input("Introduce un nombre, por favor : ")

if nombre_usuario in amigos:
    print("Hola, amigo!")

elif nombre_usuario in familia:
    print("Hola, familia!")
else:
    print("No se quien eres.")