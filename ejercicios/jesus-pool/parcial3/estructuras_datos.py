materias = ["Matematicas", "Fisica", "Quimica", "Biologia", "Historia", "Geografia", "Literatura"]
materias.append("Ingles")
materias.insert(2, "Educacion fisica")
print(materias[2])

docente =("Juan perez", "Fulanito perez", "Perecila sanchez")
print(docente[0])

conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.add(6)
print(conjunto)

alumno = {"nombre": "carlos", "edad":20, "carrera": "ingenieria"}
print(alumno["nombre"])
print(alumno["edad"])

print(materias)
lista_conjunto = list(conjunto) #Convirtiendo el conjunto a una lista
conjunto_materias = set(materias) #Convirtiendo la lista de materia a un conjunto
print(conjunto_materias)