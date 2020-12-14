miLista = ["Maria", "Eduardo", "Jesus", "Rubi", "Aurelio", "Javier"]
miLista2 = ["Roman", "Marina", 678] * 3 # El asterisco funciona como repetidor

miLista3 = miLista + miLista2

miLista.append("Roxana")
miLista.append("Mariana")
miLista.insert(2,"Monica")
miLista.extend(["Federico", "Manuel", "Sandra", "Lucia"])
miLista.extend([5, True, 56.7, 45, False])
miLista.remove(False)
miLista.pop() # Elimina el ultimo elemento.


print(miLista[:])
print(miLista[2])
print(miLista[:3])
print(miLista[3:6])
print(miLista[4:])
print(miLista.index(("Sandra")))
print("Andrea" in miLista)
print(True in miLista)
print(56.7 in miLista)
print(miLista2)
print(miLista3)