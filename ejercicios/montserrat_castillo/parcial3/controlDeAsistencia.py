#contador de asistencia
"""
Control de asistencias

En una escuela se desea crear un pequeño sistema para registrar:
1. Nombre de alumnos que asistieron a clases.
2. Materias favoritas de cada alumno.

Sin embargo algunos alumnos escribieron su nombre más de una vez por error.

Tu tarea será organizar la información utilizando diferentes estructuras de datos.
"""

asistencias = ["José", "Miguel", "Montserrat"]
alumnos_unicos = set(asistencias)
print("Alumnos que asistieron sin repetir:", alumnos_unicos)

materias_favo = {"José": "Matematicas", "Miguel": "Historia", "Montserrat": "Español"}

reporte_final = []
for alumno in alumnos_unicos:
    materias = materias_favo.get(alumno, "No registro")
    reporte_final.append((alumno, materias))

print("\n2. Reporte final de asistencia y materias:")
for alumno, materia in reporte_final:
    print(f"Alumno: [{alumno}] Materia favorita: [{materia}]")