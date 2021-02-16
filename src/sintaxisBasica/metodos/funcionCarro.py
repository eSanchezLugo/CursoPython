carros =[{
        "marca" : "Ford",
        "modelo" : "Fiesta",
        "kilometraje": 23000,
        "total_combustible" : 460
        },
        {
        "marca" : "Ford",
        "modelo" : "Focus",
        "kilometraje": 17000,
        "total_combustible" : 350
        },
        {
        "marca" : "Mazda",
        "modelo" : "MX-5",
        "kilometraje": 49000,
        "total_combustible" : 900
        },
        {
        "marca" : "Mini",
        "modelo" : "Cooper",
        "kilometraje": 31000,
        "total_combustible" : 235
        }
        
] 

def calcular_millas(carro):

    mpg = carro["kilometraje"]/ carro ["total_combustible"]
    return mpg


def nombre_carro(carro):
    nombre = f"{carro['marca']} {carro['modelo']}"
    return nombre


def informacion_carro(carro):
    nombre = nombre_carro(carro)
    mpg = calcular_millas(carro)
    
    return f"{nombre} hace {mpg} millas por galon. "


for carro in carros:

    print (informacion_carro(carro))