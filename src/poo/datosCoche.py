class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False


    def arrancar(self):
        self.arrancado = True
    
    def estadoCoche(self):
        if (self.arrancado):
            return "El coche está funcionando"
        else:
            return "El coche esta parado"

mazda = Coche()

renault = Coche()

print("Tu coche tiene : " + str(mazda.ruedas) + " ruebdas")
mazda.arrancar()
print(mazda.estadoCoche())
