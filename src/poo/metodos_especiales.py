class Estuduante:
    def __init__(self, nombre):
        self.nombre = nombre
        

peliculas = ['Nemo', 'Piratas del caribe']
print(peliculas.__class__)
print("hola".__class__)


class Carros:
    def __init__(self):
        self.carro = []
    
    def __len__(self):
        return len(self.carro)
    
    def __getitem__(self, i):
        return self.carro[i]
    
    def __repr__(self):
        return f'<Carros {self.carro}>'
    
    def __str__(self):
        return f'Carros con {len(self)} carros.'

ford = Carros()
ford.carro.append('Fiesta')
ford.carro.append('Focus')

print(len(ford))
print(ford[0])

for carro in ford:
    print(carro)
    
print(ford)