miDiccionario = {"Ciudad de México": "Toluca", "Colombia": "Bogota", "USA": "Washington"}

valor = miDiccionario.setdefault("Ciudad de México", "No existe la clave")

print(valor)