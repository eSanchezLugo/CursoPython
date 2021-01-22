class Persona():
    nombre = ""
    apellido = ""
    edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero


    def hablar(self):
        return " La persona que se llama : " + self.nombre + " está hablando"
    
    def camina(self):
        return " La persona que se llama : " + self.nombre + " está caminando"
    
    def getDatos(self):

        return "Nombre : " + self.nombre + " Apellido : " + self.apellido + \
            " Edad : " + str(self.edad) + " Genero : " + self.genero

p1 = Persona("Eduardo", "Sanchez", 29, "Masculino")

print(p1.getDatos())

