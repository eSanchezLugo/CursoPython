
nombre = input("Introduce tú nombre por favor: ")
print("Tú nombre tiene: str(len(nombre)) letras")

nombre = input("Introduce tú nombre por favor: ")
print(f"Tú nombre tiene: {len(nombre)} letras")

name = "Eduardo"
final_mensaje = "¿Comó estás?, {}"
eduardo_mensaje = final_mensaje.format(name)
print(eduardo_mensaje)

alejandro_mensaje = final_mensaje.format("Alejandro")
print(alejandro_mensaje)

mi_nombre = "Eduardo"
tu_nombre = input("Ingresa tu nombre, por favor :")

print(f"Hola {tu_nombre}. Mi nombre es {mi_nombre}.")