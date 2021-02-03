edad_amigos = {"Manuel": 28, "Rosa": 29, "Luis": 35, "Ana": 45}

print( "La edad de Ana es : " + str(edad_amigos["Ana"]))

edad_amigos["Alejandro"] = 21

print(edad_amigos)

edad_amigos["Manuel"] = 40

print(edad_amigos)


amigos = (
    {"Nombre": "Osvaldo", "Edad": 37},
    {"Nombre": "Javier", "Edad": 28},
    {"Nombre": "Esmeralda", "Edad": 26},
    {"Nombre": "Fabiola", "Edad": 21}
)

print(amigos[0]["Nombre"])
print(amigos[2]["Edad"])

conocidos = [("Marlene", 34), ("Jose", 23), ("Alberto", 31), ("Miguel", 29)]
conocidos_edad = dict(conocidos)
print(conocidos_edad)