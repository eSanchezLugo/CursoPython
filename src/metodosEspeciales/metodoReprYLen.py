import datetime

class Persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    

    #def __str__(self):
        #return "Datos de la persona: \n  Nombre : " + self.nombre + "\n Apellido : " + self.apellido + "\n Edad : " + str(self.edad)

    
    def __repr__(self): # Es más precisa la información.
        return "Datos de la persona: \n Nombre : " + self.nombre + "\n Apellido : " + self.apellido + "\n Edad : " + str(self.edad)

p1 = Persona("Eduardo", "Sánchez", 29)
print(p1)


print("---------------------------------------------------------------------------")

hoy = datetime.date.today()

print(str(hoy))
print(repr(hoy))

print("---------------------------------------------------------------------------")


class Agenda():

    def __init__(self):

        self.miAgenda = {}

    
    def agregar_personas(self, nombre_persona, telefono):

        self.miAgenda[nombre_persona]=telefono
    
    def obtener_informacion(self):

        return self.miAgenda

    def __len__(self):

        return len(self.miAgenda)



agendaPersonal = Agenda()

agendaPersonal.agregar_personas("Eduardo", "5510910774")
agendaPersonal.agregar_personas("María", "551089325675")
agendaPersonal.agregar_personas("Roxana", "5512456774")
agendaPersonal.agregar_personas("Pedro", "551599325675")
agendaPersonal.agregar_personas("Enrique", "5623680774")
agendaPersonal.agregar_personas("Alicia", "551092192395")

print(len(agendaPersonal))
print(agendaPersonal.obtener_informacion())


