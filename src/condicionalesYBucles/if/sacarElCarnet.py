print("Obtención carnet de conducir")
edad=int(input("Introuducetu edad, por favor : "))
vision=input("¿Tienes la visión correcta? : ")

if edad>=18 and edad<90 and vision=="si":
    print("Puedes intentar obtener el carnet")
else: 
    print("Lo siento. No cumples con la edad necesaria")