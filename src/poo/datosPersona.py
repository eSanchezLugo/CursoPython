class Persona():
    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero
    

    def setEdad(self, laEdad):
        if laEdad <0 or laEdad>100:
            print ("Error en la edad")
        else:
            self.__edad = laEdad
            return self.__edad


    def hablar(self):
        return " La persona que se llama : " + self.__nombre + " está hablando"
    
    def camina(self):
        return " La persona que se llama : " + self.__nombre + " está caminando"
    
    def getDatos(self):

        return "Nombre : " + self.__nombre + " Apellido : " + self.apellido + \
            " Edad : " + str(self.__edad) + " Genero : " + self.genero

p1 = Persona("Eduardo", "Sanchez", "Masculino")
p1.setEdad(29)
print(p1.getDatos())
p2 = Persona("Alejandro", "Lugo", "Masculino")
print(p2.getDatos())
p1.setEdad(120)
p2.nombre = "Alicia"
print(p2.getDatos())


