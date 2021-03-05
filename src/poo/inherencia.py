class Estudiante:
    def __init__(self, nombre, escuela):
        self.nombre = nombre
        self.escuela = escuela
        self.calificaciones = []
        
    @property
    def promedio(self):
        return sum(self.calificaciones)/ len(self.calificaciones)
    

class EstudianteTrabaja(Estudiante):
    def __init__(self, nombre, escuela, salario):
        super().__init__(nombre, escuela)
        self.salario = salario
    
    @property # este nos ayuda a crearlo como propiedad ya que no tiene argumentos, o en algo que podamos acceder.
    def salario_semanal(self):
        return self.salario * 37.5
    
eduardo = EstudianteTrabaja('Eduardo', 'MIT', 15.50)
print(eduardo.salario)
eduardo.calificaciones.append(57)
eduardo.calificaciones.append(99)
#print(eduardo.promedio())
print(eduardo.promedio)
#print(eduardo.salario_semanal())
print(eduardo.salario_semanal)


jesus = Estudiante('Jesus', 'Oxford')
jesus.calificaciones.append(99)
jesus.calificaciones.append(60)

print(jesus.promedio)

    