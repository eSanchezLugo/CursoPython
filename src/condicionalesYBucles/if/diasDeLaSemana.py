diaSemana = input("Ingresa un día de la semana : ")

if diaSemana.lower() == "lunes":
    print("Es un día para comenzar con toda la energía del mundo.")
elif diaSemana.lower() == "viernes":
    print("Animo ya es el utimo dia para descansar")
elif diaSemana.lower() == "sabado" or diaSemana.lower() == "domingo":
    print("Realizar tus jobis preferidos y olvidarte del trabajo")
else :
    print("Ya falta poco para descansar del trabajo")