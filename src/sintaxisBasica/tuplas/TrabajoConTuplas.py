misDatos = ("Eduardo",23,4, 2000)

misDatosLista = list(misDatos) #Se convierte de una tupla a lista.
print(misDatosLista)

datosPersona = ["Alejandro", 23, 12,2002, "Eduardo", "Mariana", 23, 30, "Alejandro", "Eduardo", "Alejandro"]

miNuevaTupla = tuple(datosPersona) # Se convierte de una lista a tupla.
print(miNuevaTupla)
print (25 in miNuevaTupla)
print("Alejandro" in miNuevaTupla)
print(miNuevaTupla.count("Alejandro"))
print(len(miNuevaTupla))


# Desempaquetado de tuplas

nombre, dia, mes, anio = misDatos
print(nombre)
print(anio)



