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

