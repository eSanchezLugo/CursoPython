def evaluarAlumno(nota):
    valoracion = "Desconocida"
    if nota<5:
        valoracion = "Reprobado"
    elif nota > 10:
        valoracion = "Nota incorrecta"
    else:
        valoracion = "Aprobado"
    return valoracion


notaAlumno = int(input("Ingresa tu calificación, por favor : "))
print(evaluarAlumno(notaAlumno))



