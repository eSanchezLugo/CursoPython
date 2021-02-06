edades = [22, 35, 27, 21, 20, 29, 67, 78]
edades_conocidos = [edad for edad in edades if edad %2 == 1]

print(edades_conocidos)

print("--------------------------------------------------------------------------------")

amigos = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier", "Delia", "Rosa", "Elizabeth", "Daniel", "Miguel"]
invitados = ["merlin", "Felipe", "Rolf", "Bob", "Karen", "Miguel", "Rosa", "Daniel"]



amigos_que_se_presentan = [
    nombre.title() 
    for nombre in invitados 
    if  nombre.lower() in [amigo.lower() for amigo in amigos]
]



print(amigos_que_se_presentan)