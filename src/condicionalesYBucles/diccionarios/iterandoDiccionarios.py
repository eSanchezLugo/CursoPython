amigos_edades = {"Rosa": 30, "Manuel": 23, "Esmeralda": 32, "Tania": 21, "Bob": 43, "Alberto": 32}



for nombre in amigos_edades:
    print(nombre)

print("-----------------------------------------")

for edad in amigos_edades.values():
    print(edad)

print("-----------------------------------------")

for nombre, edad in amigos_edades.items():
    print(f"{nombre} tiene {edad} años.")
