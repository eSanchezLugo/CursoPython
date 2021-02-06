amigos = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier", "Delia", "Rosa", "Elizabeth", "Daniel", "Miguel"]
invitados = ["merlin", "Felipe", "Rolf", "Bob", "Karen", "Miguel", "Rosa", "Daniel"]


amigos_minusculas = {amigo.lower() for amigo in amigos}
invitados_minusculas = {invitado.lower() for invitado in invitados}

interseccion_amigos = amigos_minusculas.intersection(invitados_minusculas)
amigos_que_se_presentan = {nombre.title() for nombre in interseccion_amigos}

print(amigos_que_se_presentan)

print("--------------------------------------------------------------------------------")

amigos = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier", "Delia", "Rosa", "Elizabeth", "Daniel", "Miguel"]
tiempo_de_no_vernos = [3, 7, 15, 11, 1, 12, 34, 1, 6, 7, 9]

largo_tiempo = {

    amigos[i] : tiempo_de_no_vernos[i]
    for i in range(len(amigos))
        if tiempo_de_no_vernos[i] > 5

}
print(largo_tiempo)


print("--------------------------------------------------------------------------------")

amigos = ["Diana", "Jesús", "Rubí", "Roxana", "Aurelio", "Javier", "Delia", "Rosa", "Elizabeth", "Daniel", "Miguel"]
tiempo_de_no_vernos = [3, 7, 15, 11, 1, 12, 34, 1, 6, 7, 9]



largo_tiempo = list(zip(amigos, tiempo_de_no_vernos, [1, 4, 5, 1, 11, 22, 34, 4, 2, 17, 11]))

print(largo_tiempo)