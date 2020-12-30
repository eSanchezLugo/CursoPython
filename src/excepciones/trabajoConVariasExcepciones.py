def divide():
    try:
        op1=(float(input("Introduce el primer número, por favor : ")))
        op2=(float(input("Introduce el segundo número, por favor : ")))
        print("El resutlado es : " + str(op1/op2))
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print(" El valor introducido no es numérico")
    finally:
        print("Se ha intentado ejecutar la función en su totalidad")

divide()
print("Cálculo finalizado. Continuamos con el programa")