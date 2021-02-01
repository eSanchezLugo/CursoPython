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

        Persona.__init__(self,nombre, apellido, edad) # Mando a llamar el constructor padre.
        self.escuela = escuela

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudiar(self):

        return "Estoy estudiando"



class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):

        Persona.__init__(self, nombre, apellido, edad) # Mando a llamar el constructor padre.
        self.empresa = empresa

    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Empresa: " + self.empresa

    def trabaja(self):

        return "Estoy trabajando"


class Director(Trabajador, Estudiante): # Herencia multiple, mientras mas a la izquierda este la clase a heredar, tendra mas preferencia.

    def __init__(self,nombre, apellido,edad, empresa, escuela, bonus):

        Trabajador.__init__(self, nombre, apellido,edad, empresa)

        Estudiante.__init__(self,nombre,apellido,edad,escuela)


        self.bonus = bonus
    
    def  getDatosPersonales(self):

        return super().getDatosPersonales() + " Bonus : " + str(self.bonus)
    
    def dirige(self):

        return "Estoy dirigiendo"


persona = Persona("Eduardo", "Sanchez", 29)
estuduante = Estudiante("Alejandro", "Lugo", 29, "Juan de Dios")
trabajador = Trabajador ("Federico", "Fernandez", 29, "Cope")
director = Director("Felix", "Mendez", 45, "Patito", "x", 2000000)

print(persona.getDatosPersonales())
print(estuduante.getDatosPersonales())
print(trabajador.getDatosPersonales())
print(director.getDatosPersonales())