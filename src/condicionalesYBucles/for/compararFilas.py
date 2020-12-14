import random

miLista1 = ["Maria", "Eduardo", "Adriana", "Marlene"]
miLista2 =  ["Maria", "Eduardo", "Adriana", "Marlene"]

def compararListas (miLista1, miLista2):
    if(len(miLista1) != len(miLista2)):
        return False
    else:
        for i in range(0,len(miLista1)):
            if (miLista1[i] != miLista2[i]):
                
                return False
    
    return True

print(compararListas(miLista1, miLista2))