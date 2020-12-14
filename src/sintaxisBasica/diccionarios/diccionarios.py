miDiccionario = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres", "España": "Madrid"}
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario["Francia"])
print(miDiccionario)
miDiccionario["Italia"]= "Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)

miDiccionario2 = {"Alemania": "Berlin", 23 : "Jordan", "Mosquetero": 3}
print(miDiccionario2)

miTupla = ("España", "Francia","Reino Unido", "Alenania")
miDiccionario3 = {miTupla[0] : "Madrid", miTupla[1]: "Londres", miTupla[2] : "Londres", miTupla[3] : "Berlin"}
print(miDiccionario3["Francia"])

miDiccionario4 = { 23:"Jordan","Nombre": "Michael", "Equipo" : "Chicago", "Anillos": (1991,1992,1993,1996,1997,1998) }
print((miDiccionario4))
print(miDiccionario4["Equipo"])
print(miDiccionario4["Anillos"])

# Guardar un diccionario dentro de otro diccionario y en los años que gano es una tupla.
miDiccionario5 = { 23:"Jordan","Nombre": "Michael", "Equipo" : "Chicago", "Anillos":{"Temporadas": (1991,1992,1993,1996,1997,1998) }}
print(miDiccionario5 ["Anillos"])
print(miDiccionario5.keys())
print(miDiccionario5.values())
print(len(miDiccionario5))
print(miDiccionario5.keys())
print(miDiccionario5.values())
print(len(miDiccionario5)) 