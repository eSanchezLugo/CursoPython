def capitales_mundo(*ciudades):
    # * numero indeterminado de parametros y lo almacena en una tupla.
    for capital in ciudades:
        #for letraCapital in capital:
            #yield letraCapital
        yield from capital
  

capitales_devueltas = capitales_mundo("Berlín", "Roma", "Bogotá", "Pekín", "Hanoi")

print (next(capitales_devueltas))
print (next(capitales_devueltas))
print (next(capitales_devueltas))