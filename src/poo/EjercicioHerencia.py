class Vehiculo():

    def __init__(self, color, ruedas, ancho, alto,marchas):

        self.color = color
        self.ruedas = ruedas
        self.ancho = ancho
        self.alto = alto
        self.marchas = marchas
        self.acelerando = False
        self.frenando = False
        self.girando = False

    def Acelerar(self):

        self.acelerando = True
    
    def Frenar(self):

        self.frenando = True


    def Girardo(self):

        self.girando = True

    def getDatosVehiculo(self):

            return "Color : " + self.color + " Ruedas : " + str(self.ruedas) + " Ancho : " + str(self.ancho) + " cm "\
                + " Alto : " + str(self.alto) +  " cm " + " Número de marchas : " + str(self.marchas)
    

    
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, ancho, alto, marchas,cilindrada, asientos, aire_acondicionado):

        super().__init__(color, ruedas, ancho, alto, marchas)
        self.cilindrada = cilindrada
        self.asientos = asientos
        self.aire_acondicionado = aire_acondicionado
    
    def Ir_Marcha_Atras(self):

        self.marcha_atras = True
    
    def Arrancar(self):

        self.arrancar = True

    def getDatosCoche(self):

        return super().getDatosVehiculo() + " Número de cilindros " + str(self.cilindrada)\
            + " Número de asientos : " + str(self.asientos) + " Tiene aire acondicionado : " + self.aire_acondicionado

class Furgoneta(Coche):

    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos, aire_acondicionado, cargar):
        
        super().__init__(color, ruedas, ancho, alto, marchas,cilindrada, asientos, aire_acondicionado)
        self.cargar = cargar

    
    def Cargar(self):

        self.cargar = True

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas,ancho, alto, marchas):

        super().__init__(color, ruedas,ancho, alto, marchas)
    
    def Saltar(self):

        self.saltar = True
    
    def Derrapar(self):

        self.derrapar = True

    def getDatosBicicleta(self):

        return super().getDatosVehiculo()


class Motocicleta(Coche, Bicicleta):

    def __init__(self, color, ruedas,ancho, alto , marchas, cilindrada, asientos, aire_acondicionado):
        
        super().__init__(color, ruedas, ancho, alto, marchas, cilindrada, asientos, aire_acondicionado)




vehiculo = Vehiculo("Azul", 4, 160, 30, 1)
print(vehiculo.getDatosVehiculo())
coche = Coche("Verde", 4, 200, 60, 1, 8, 4, "Si")
print(coche.getDatosCoche())
bicicleta = Bicicleta("Naranja", 2, 100, 20, 1)
print(bicicleta.getDatosBicicleta())
