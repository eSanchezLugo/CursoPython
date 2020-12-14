print ("Devuelve el número maximo")

primer_numero = int(input("Ingresa el primer número, por favor :"))
segundo_numero = int(input("Ingresa el segundo número, por favor :"))

def DevuelveMax (primer_numero, segundo_numero):

    if primer_numero < segundo_numero :
        print("El segundo número es mayor")
    elif segundo_numero < primer_numero :
        print("El primer número es mayor")
    else:
        print(" Los números son iguales")

DevuelveMax(primer_numero,segundo_numero)