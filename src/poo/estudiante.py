estudiante = {
    'nombre': 'Eduardo Sanchez',
    'calificaciones': [70, 88, 90, 99]

}

def  calificaciones_promedio(estudiante_1):
    return sum(estudiante_1['calificaciones'])/ len(estudiante_1['calificaciones'])

class Estudiante :
    
    
    def __init__(self, nuevo_nombre, nueva_calificacion):
        self.nombre = nuevo_nombre
        self.calificaciones = nueva_calificacion


    def promedio_alumno(self):
        return sum(self.calificaciones)/ len(self.calificaciones)

estudiante_uno = Estudiante('Rubi Zaragoza', [70, 88, 90, 99])
print(f"{estudiante_uno.nombre} , {estudiante_uno.promedio_alumno()}") 