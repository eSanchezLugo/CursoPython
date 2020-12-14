paises = {}

pais = input("Introduce un pais, por favor :")

while pais != "salir":

    ciudades = input ("Introduce una ciudad, por favor : ")
    lista_ciudades = paises.setdefault(pais,[ciudades])
    if lista_ciudades != [ciudades]:
        paises[pais].append(ciudades)
    pais = input("Introduce un pais, por favor : ")

print(paises)




