carros = ["OK.","OK.","OK.", "defectuoso", "OK.","OK."]


for status in carros:
    if status == "defectuoso":
        print("Coche defectuoso encontrado...")
        continue

    print(f"Este carro esta {status}.")
    print("Enviamos un auto nuevo al cliente!")



    
