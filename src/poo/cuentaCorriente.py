class CuentaCorriente():
    numero_cuenta ="16" 
    nombre_titular = ""
    saldo_cuenta =0 

    def __init__(self, nombre_titular, numero_cuenta, saldo_cuenta):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta
    

    def getDatosCuenta(self):

        return "El nombre del titular es : " + self.nombre_titular +\
                " con número de cuenta : " + self.numero_cuenta  +\
                " tiene un saldo de :" + str(self.saldo_cuenta)
    
    def ingresarMonto(self, monto_ingresado):

        self.saldo_cuenta = self.saldo_cuenta + monto_ingresado
    

    def retirarDinero(self, monto_retirado):

        if monto_retirado <= self.saldo_cuenta:
            self.saldo_cuenta = self.saldo_cuenta - monto_retirado
        else:

            insuficiente = self.saldo_cuenta = monto_retirado - self.saldo_cuenta
            print("Saldo insuficiente, para poder sacar el monto ingresado te falta : " + str(insuficiente))



datosCuenta = CuentaCorriente("Eduardo Alejandro Sánchez Lugo", "4323678712456789", 400000)
datosCuenta.ingresarMonto(599999)
datosCuenta.retirarDinero(1000000)
print(datosCuenta.getDatosCuenta())

    
    
    




