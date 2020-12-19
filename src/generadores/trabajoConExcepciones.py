def suma (num1, num2):
    return num1 + num2

def resta (num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2

    except  ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"


while True :
    try:
        opcion1 =(int(input("Introduce el primer número, por favor : ")))
        opcion2 =(int(input("Introduce el segundo número, por favor : ")))
        break
    except ValueError:
        print("Los valores introducidos no son correctos")



operacion = input("Introduce la operación a realizar por favor (suma, resta,multiplicacion, divide) : ")

if operacion == "suma":
    print(suma(opcion1, opcion2))
elif operacion == "resta":
    print(resta(opcion1,opcion2))
elif operacion == "multiplica":
    print(multiplica(opcion1,opcion2))
elif operacion == "divide":
    print(divide(opcion1,opcion2))
else:
    print("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")