menu_principal = "\nIndresa 'a' para agregar una película, 'l' para ver sus películas, 'f' para buscar sus películas por título o 'q' para salir :\n"

peliculas = []


def agregar_pelicula():
    titulo = input("Ingresa el título de la película : ")
    director = input("Ingresa el director de la película : ")
    year = input("Ingresa el año en que la realizo : ")


    peliculas.append({
        'titulo' : titulo,
        'director': director,
        'year': year
    })

def ver_peliculas():
    for pelicula in peliculas:
        imprimir_pelicula(pelicula)

def imprimir_pelicula(pelicula):
    print(f"Titulo: {pelicula['titulo']}")
    print(f"Director: {pelicula['director']}")
    print(f"Año: {pelicula['year']}")


def  buscar_pelicula():
    buscar_titulo = input("Ingresa el título de la película : ")

    for pelicula in peliculas:
        if pelicula['titulo'] == buscar_titulo:
            imprimir_pelicula(pelicula)
        else:
            print("No se encontro la película")


opciones_usuario = {
    "a" : agregar_pelicula,
    "l" : ver_peliculas,
    "f" : buscar_pelicula
}
def menu():
    selecciona = input(menu_principal)
    while selecciona != 'q':
        if selecciona in opciones_usuario:
            selecciona_funcion = opciones_usuario[selecciona]
            selecciona_funcion()
        else:
            print('comando desconocido. Inténtalo de nuevo.')
        
        selecciona = input(menu_principal)


menu()