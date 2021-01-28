class Persona():

    def __init__(self, nombre, apellido, edad): #constructor.

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)
    
    def hablar(self):

        return "Estoy hablando"
    
    def pensar(self):

        return "Estoy pensando"
    
    def camina(self):

        return "Estoy caminando"
    
    def comer(self):

        return "Estoy comiendo"
    

class Estudiante(Persona): # Heredo dentro de los paréntesis.

    def __init__(self, nombre, apellido, edad, escuela):

        super().__init__(nombre, apellido, edad) # Mando a llamar el constructor padre.
        self.escuela = escuela

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudiar(self):

        return "Estoy estudiando"

persona1 = Persona("Eduardo", "Sanchez", 29)
estuduante1 = Estudiante("Alejandro", "Lugo", 29, "Juan de Dios")

print(persona1.getDatosPersonales())
print(estuduante1.getDatosPersonales())