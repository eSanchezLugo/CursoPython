Materias = ["Matemáticas","Física","Química","Historia","Lengua"]
print(Materias)

for Materias in Materias:
    print("Yo estudio : " + Materias)


MateriasEvaluadas = ["Matemáticas","Física","Química","Historia","Lengua"]

Matematicas =input("Introduce tu calificación de Matemáticas: ")
Fisica = input("Introduce tu calificación de Física : ")
Quimica = input("Introduce tu calificación de Química : ")
Historia = input("Introduce tu calificación de Historia : ")
Lengua = input("Introduce tu calificación de Lengua : ")

print("En " + " " + MateriasEvaluadas[0] + " " + "has sacado : " + Matematicas)
print("En " + " " + MateriasEvaluadas[1] + " " + "has sacado : " + Fisica)
print("En " + " " + MateriasEvaluadas[2] + " " + "has sacado : " + Quimica)
print("En " + " " + MateriasEvaluadas[3] + " " + "has sacado : " + Historia)
print("En " + " " + MateriasEvaluadas[4] + " " + "has sacado : " + Lengua)

Calificacion = []
for MateriasCalificadas in MateriasEvaluadas :
    Promedio = input("¿Que calificación sacaste en " + MateriasCalificadas + "? ")
    Calificacion.append(Promedio)
for i in range(len(MateriasEvaluadas)):
    print("En " + MateriasEvaluadas[i] + " has sacado " + Calificacion[i])