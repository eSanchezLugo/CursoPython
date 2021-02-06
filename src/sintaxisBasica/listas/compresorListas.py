numeros = [0, 1, 2, 3, 4]
doblar_numeros = []

for numero in numeros:
    doblar_numeros.append(numero * 2)

print(doblar_numeros)

print("--------------------------------------------------------------------------------")
#Realiza lo mismo que arriba, forma acortada.

doblar_numeros =[numero * 2 for numero in range(5)]
print(doblar_numeros)

print("--------------------------------------------------------------------------------")

edades_amigos = [22, 31, 35, 37]

cadena_edad = [f"Mi amigo tiene {edad} años." for  edad in edades_amigos]

print(cadena_edad)

print("--------------------------------------------------------------------------------")

nombres = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier"]
nombres_en_minusculas = [nombre.lower() for nombre in nombres]
print(nombres_en_minusculas)
nombres_en_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_en_mayusculas)

print("--------------------------------------------------------------------------------")

amigo = input("Ingresa el nombre de tú amigo, por favor : ")
amigos = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier", "Delia", "Rosa", "Elizabeth", "Daniel", "Miguel"]
amigo_minusculas = [nombre.lower() for nombre in amigos]

if amigo.lower() in amigo_minusculas:
    print(f"{amigo.title()} es uno de tus amigos.")#title : su finalidad es poner la primera letra en mayuscula y las demas un minusculas.


