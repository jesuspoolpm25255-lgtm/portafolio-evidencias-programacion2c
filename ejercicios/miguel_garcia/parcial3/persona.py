"""
crea una clase persona con ls siguientes atributos: nombre, edad, genero y
nacionalidad
Agrega un metodo para imprimir los datos de la persona y otro metodo para
calcular el año
de nacimiento de la persona.
crea un objeto de la clase personal y utiliza los metodos para mostrar
su informacion y
calcula su año de nacimiento
"""

import datetime

class Persona:
    def __init__(self, nombre, edad, genero, nacionalidad = "mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad

    def imprimirDatos(self):
        print("-----informacion-----")
        print(f"nombre: {self.nombre}")
        print(f"genero: {self.genero}")
        print(f"edad: {self.edad} años")
        print(f"nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad

def main():
    objPersona = Persona("Marco Bonilla", 38, "masculino")
    objPersona.imprimirDatos()
    print(f"Año de nacimiento: {objPersona.calcularNacimiento()}")

if __name__ == "__main__":
    main()