trabajadores = ["Paula", "Manuel", "Pedro", "Ana", "Sandra"]

if "Pedro" in trabajadores:
    print("Si, Pedro se encuentra en la lista.")
else:
    print("Pedro no se ha encontrado en la lista.")


lenguajes_Trim1 = "Java, Python,PHP, C#, HTML,JavaScript,SQL"
# Tambin se puede buscar caracteres.
if "PHP" in lenguajes_Trim1:
    print("PHP está.")
else:
    print("PHP no está.")

if "SQL" not in lenguajes_Trim1:
    print("Falta SQL en la lista.")
else:
    print("SQL está en la lista.")