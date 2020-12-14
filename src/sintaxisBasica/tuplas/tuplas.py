miTupla = ("Eduardo", "Manuel", "Alejandro",5,True, 56.8,5,"Marcelo", 5)
miLista2 = ["Mariana", 45, 678.87,False, "Rodrigo"]
miLista = list(miTupla) # convierte una tupla en lista.
miTupla2 = tuple(miLista2) # Convierte una tupla en lista.
miTupla3 = ("Eduardo",) # Tupla unitaria forsozamente debe de llevar la coma.
miTupla4 = "Alejandro",56,78.9,True,False,"Marco"

datosPersonales = ("Eduardo",23,4,1991)
nombre, dia,mes, anio = datosPersonales #Desempaquetado de tuplas.


print(miTupla[2])
print(miLista)
print(miTupla2)
print("Mariana" in miTupla2)
print("Mariana2" in miTupla2)
print(miTupla.count(5))
print(len(miTupla))
print(miTupla3)
print(miTupla4)
print(nombre)
print(anio)
print(dia)
print(mes)
print(miTupla4.index("Marco"))