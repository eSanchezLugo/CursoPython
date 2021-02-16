
operaciones ={

    "promedio": lambda secuencia: sum(secuencia) / len(secuencia),
    "total" : lambda secuencia: sum(secuencia),
    "top" : lambda secuencia : max (secuencia)

}


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


for estudiante in estudiantes : 
    nombre = estudiante["nombre"]
    calificaciones = estudiante["calificaciones"]

    print(f"Estudiante: {nombre}")
    operacion = input ("Entre 'promedio', 'total',  o 'top' : ")

    operacion_deseada = operaciones[operacion]
    print(operacion_deseada(calificaciones))