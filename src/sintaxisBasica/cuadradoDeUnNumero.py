def cuadradoNumero():
    numero_cuadrado = int(input("Introduce el número a elevar, por favor : ")) 
    print(f"El resultado del número al cuadrado es : {numero_cuadrado * numero_cuadrado} ")

cuadradoNumero()


def cuadrado (numero):
    cua = numero * numero
    return cua

print("El resultado del número al cuadrado es : " + str(cuadrado(5)))


for x in range(2,9):
    print (cuadrado(x))