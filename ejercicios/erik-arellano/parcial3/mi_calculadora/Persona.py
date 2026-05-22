"""
Crea una clase Persona con los siguientes atributos: nombre, edad, género y nacionalidad.
Agrega un método para imprimir los datos de la persona y otro método para calcular el año
de nacimiento de la persona.
Crea un objeto de la clase Persona y utiliza los métodos para mostrar su información y
calcular su año de nacimiento.
"""
import datetime

class Persona:

    def _init_(self, nombre, edad, genero, nacionalidad = "México"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero 
        self.nacionalidad = nacionalidad

    def informacion(self):
        print("------Información------")
        print(F"{self.nombre} ({self.genero})")
        print(f"Edad: {self.edad} años")
        print(f"Nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad
    
def main():
    objPersona = Persona("Erik Cruz", 15,"Masculino")
    objPersona.informacion()
    print(f"Año de nacimiento: {objPersona.calcularNacimiento()}")

if __name__ == "__main__":
     main()