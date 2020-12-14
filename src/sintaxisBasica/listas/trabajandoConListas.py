trabajadores = ["Ana", "Maria", "Antonio", "Miguel"]


trabajadores.append("Eduardo")
trabajadores.append("34")

print(trabajadores)
print(trabajadores[2])
print(trabajadores[-2])
print(trabajadores[0:3])
print(trabajadores[2:4])
print(trabajadores[3:2])


trabajadores.extend(["Alejandro",5,23,56.6,True, False, "Marina", "Eduardo", 5, 23])

print(trabajadores)

print(trabajadores.index("Alejandro"))
print(trabajadores.count("Eduardo"))
print(trabajadores.count(5))

trabajadores.reverse()

print(trabajadores)

trabajadores.remove("Eduardo")

print(trabajadores)


trabajadores_edificio1 = ["Ana","Antonio","Maria", "Pedro", "Laura"]
trabajadores_edificio2 = ["Jorge","Francisco","Patricia","Óscar"]

print(trabajadores_edificio1 + trabajadores_edificio2)

del trabajadores_edificio1[0]
print(trabajadores_edificio1)


