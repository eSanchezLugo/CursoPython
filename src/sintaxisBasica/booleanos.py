numero_magico = 20
numero_usuario = int(input("Introduce un número, por favor : "))
print (numero_magico == numero_usuario)

edad = int(input("Ingresa tu edad, por favor : "))
edad_suficiente = edad > 0 and edad < 100
print(f"Puedes aprender a programar: {edad_suficiente}.")

edad = int(input("Ingresa tu edad, por favor : "))
usuario_trabaja = edad < 18 or edad > 65
print(f"{edad} usualmente estas trabajando : {usuario_trabaja}.")

nombre = ""
apellido = "Sánchez"

saludar = nombre or f"Mr. {apellido}"
print(saludar)
