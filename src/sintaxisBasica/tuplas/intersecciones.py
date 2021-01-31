amigos_artistas = {"Rodolfo", "Roxana", "Jesus", "Manuel"}
amigos_cientificos = {"Javier", "Florencia", "María", "Fernanda", "Manuel"}

artistas_y_cientificos = amigos_artistas.intersection(amigos_cientificos)
print(artistas_y_cientificos)

todos_los_amigos = amigos_artistas.union(amigos_cientificos)
print(todos_los_amigos)