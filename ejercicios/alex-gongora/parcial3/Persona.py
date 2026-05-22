"""
Crea una clase persona con los siguientes atributos: nombre, edad, genero, y nacionalidad.
Agrega un metodo para imprimir los datos de una persona y el otro metodo para calcular el año
de nacimiento de la persona.
Crea un objeto de la clase de la persona y utiliza los metodos para mostrar su informacion y 
calcular su año de nacimiento. 
"""
import datetime

class Persona:

    def __init__(self, nombre, edad, genero, nacionalidad = "Mexico"):
        self.nombre = nombre
        self.edad = edad 
        self.genero = genero 
        self.nacionalidad = nacionalidad 
    
    def informacion(self):
        print("------Informacion------")
        print(f"{self.nombre} ({self.genero})")
        print(f"Edad: {self.edad} años")
        print(f"Nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad
    
    def main():
        objPersona = Persona("Alex Gongora", 16, "Maculino")
        objPersona.informacion()
        print(f"Año de nacimiento: {objPersona.calcularNacimiento()}")

    if __name__ == '__main__':
        main()  