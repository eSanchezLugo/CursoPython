def generarPares(limite):

    num= 1

    while num < limite:

        yield num * 2

        num = num+1

sucesuinPares = generarPares(6)

print(next(sucesuinPares))

print("Ahora va el siguiente valor : ")

print(next(sucesuinPares))

print("Ahora va el siguiente valor : ")

print(next(sucesuinPares))

print("Ahora va el siguiente valor : ")

print(next(sucesuinPares))

print("Ahora va el siguiente valor : ")

print(next(sucesuinPares))


