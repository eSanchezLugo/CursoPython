capitales = {"China":"Pekin", "Inidia":"Nueva Delhi","Indonesia":"Yakarta", "Japón": "Tokio", "Blangadesh": "Dacca"}

for clave in capitales:
    valor = capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())


for clave, valor in capitales.items():
    print(clave + " -> " + valor )