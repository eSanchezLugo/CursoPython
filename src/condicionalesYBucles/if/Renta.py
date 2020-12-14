
Renta = float(input("Introduce la renta : "))

if Renta < 12000 :
    impuesto = 7
elif Renta < 18000:
    impuesto = 15
elif Renta< 35000:
     impuesto = 21
elif Renta < 70000:
     impuesto = 35
else :
    impuesto = 45
    

print (" A la renta de " + str(Renta) +  " le corresponde un " + str(impuesto) + "% de impuesto")




