
nombresPersonas  = []

def agregar_persona_lista (lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error, Este nombre ya se encientra introducido", nombreIntroducido)

numeroPersona = 1 

while numeroPersona<11:

    nombre = input("Introduce el nombre, por favor : ")
    agregar_persona_lista(nombresPersonas, nombre)
    numeroPersona+=1

    print(nombresPersonas)