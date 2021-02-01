nombre_usuario = input("Introduce tu nombre, por favor : ")

print("El usuario introducido es :", nombre_usuario.upper())
print("El usuario introducido es :", nombre_usuario.lower())
print("El usuario introducido es :", nombre_usuario.capitalize())


edad_usuario = input("Introduce tu edad, por favor : ")

contador = 0
while(edad_usuario.isdigit()== False):

    print("El valor introducido no es correcto")

    edad_usuario = input("Introduce tu edad, por favor : ")

    contador += 1

    if contador >=3 :
        break

if(int(edad_usuario)< 18):

    print("No puedes pasar")

else:

    print("Puedes pasar")



