class Carro:
    def __init__(self, marca, modelo ):
        self.marca = marca
        self.modelo = modelo
    
    def __repr__(self):
        return f'<Carro {self.marca} {self.modelo}>'

class Garage:
    def __init__(self):
        self.carros = []
    
    def __len__(self):
        return len(self.carros)
    
    def agregar_carro(self, carro):
        if not isinstance(carro, Carro):
            raise TypeError(f'Intente agregar un nombre`{carro.__class__.__name__}` en el garage, pero tu puedes agregar objetos de `Carro`')
        self.carros.append(carro)
    
ford = Garage()
ford.agregar_carro('Fiesta')   
print(len(ford))