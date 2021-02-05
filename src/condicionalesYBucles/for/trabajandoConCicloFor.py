amigos  = ["Mariano", "Sebastian", "Francisco", "Vanessa"]

for amigo in amigos:
    print(amigo)


elementos =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in elementos:
    print(numero)
    


estudiantes = [

    {"Nombre": "Eduardo", "Grado": 90},
    {"Nombre": "Bob", "Grado": 78},
    {"Nombre": "Ana", "Grado": 90},
    {"Nombre": "Amanda", "Grado": 90},

]

for estuduante in estudiantes:
    nombre = estuduante["Nombre"]
    grado = estuduante["Grado"]

    print(f"{nombre} tiene un grado de {grado}.")