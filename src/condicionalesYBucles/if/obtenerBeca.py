print ("Obtener la beca de estudiante")

notaEstuduante = int(input("Introduce tu calificación, por favor : "))
hermanos_Escuela = int(input("¿Tienes hermanos en esta institución : "))
distancia_Escuela = int(input("Introduce la distancia que haces a la escula : "))
renta_familiar = int(input("Introduce la renta mensual de donde vives : "))

if (notaEstuduante > 8 and hermanos_Escuela > 3 and distancia_Escuela > 10) or renta_familiar < 20000:
    print("Se te concede la beca")
else : 
    print("Lo siento, no cumples con los requisitos ")