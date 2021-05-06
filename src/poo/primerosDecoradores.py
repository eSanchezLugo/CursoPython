class foo:
    @classmethod
    def hola(cls):
        print(cls.__name__)
        
mi_objeto = foo()
mi_objeto.hola()

class bar:
    @staticmethod
    def hola():
        print("Hola, no tomo parametros.")

otro_parametro = bar()
otro_parametro.hola()


class moneda :
    def __init__(self, cantidad):
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'<moneda {self.cantidad: .2f}>'

    @classmethod
    def suma(cls,valor_1, valor_2):
        return cls(valor_1 + valor_2)

nuevo_numero = moneda.suma(19.575, .0789)
print(nuevo_numero)
    
class Euro(moneda):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.simbolo = '€'
    
    def __repr__(self):
        return f'<Euro {self.simbolo}{self.cantidad:.2f}>'
    
    
dinero = Euro (18.786)
print(dinero)
        