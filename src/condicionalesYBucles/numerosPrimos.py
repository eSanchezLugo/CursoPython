for  numero in range (2, 101):
    for numero_primo in range(2, numero):
        if numero % numero_primo == 0:
            print(f" {numero} es igual {numero_primo} * {numero//numero_primo}.")
            break
    else:
        print(f"{numero} es un número primo.")


