class Persona():

    def hablar(self):

        return "Hablo como una persona."

class Trabajador(Persona):

    def hablar(self):

        return "Hablo con un trabajador."

class Director(Trabajador):

    def hablar(self):

        return "Hablo como un director."

def hazlesHablar(lista_de_las_personas):

    for persona in lista_de_las_personas:

        print(persona.hablar())

def hablando(objeto):

    print(objeto.hablar())

Antonio = Persona()
Maria = Trabajador()
Ana = Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("--------------------------------------------------------")

listaPersonas = [Antonio, Ana, Maria]
hazlesHablar(listaPersonas)

print("--------------------------------------------------------")

hablando(Maria)
hablando(Ana)
hablando(Antonio)
