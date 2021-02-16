promedio = lambda secuencia: sum(secuencia) / len(secuencia)

estudiantes=[
    {"nombre": "Rodrigo",
    "calificaciones": (67, 90, 95, 100)
    },
    {
    "nombre": "Julian",
    "calificaciones": (56, 78, 80, 90)
    },
    {
    "nombre": "Bob",
    "calificaciones": (98, 90, 95, 99)
    },
    {
    "nombre": "Tom",
    "calificaciones": (100, 100, 95, 100)
    }
]

for estudiante in estudiantes:
    print(promedio(estudiante["calificaciones"]))