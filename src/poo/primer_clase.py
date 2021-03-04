class Pelicula:
    
    def __init__(self,nombre, director):
        
        self.nombre = nombre
        self.director = director
    

    def informacion(self):
        print(f"<<{self.nombre}>> by {self.director}")

