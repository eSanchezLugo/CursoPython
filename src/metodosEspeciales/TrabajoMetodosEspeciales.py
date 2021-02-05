class Persona():

    def __init__(self, **datos):
        #*datos, representa un número indeterminado de datos, se convierte en una tupla.
        #**datos, crea un diccionario.

        elementos = datos.items()

        for clave, valor in elementos:
            print(clave, " ", valor)
    
persona1 = Persona(Nombre = "Eduardo", Apellido="Sánchez", Edad = 29 )
