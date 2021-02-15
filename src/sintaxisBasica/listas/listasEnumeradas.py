amigos = ["Luis", "Daniel", "Federico", "María"]

contar = 0 

for amigo in amigos : 
    print(contar)
    print(amigo)
    contar = contar + 1


for contar, amigo in enumerate(amigos):
    print(contar)
    print(amigo)

print(list(enumerate(amigos)))
print(list(zip([0,1,2,3], amigos)))
print(dict(enumerate(amigos)))