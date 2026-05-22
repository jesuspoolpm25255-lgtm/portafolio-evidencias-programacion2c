class Perro:
    #Atributos de la clase Perro
    especie = "Canus lupus familiaris"
    #Constructor de la clse perro

def __init__(self, nombre, raza = "Caramelo", edad = 0):
        self.nombre= nombre
        self.raza= raza
        self.edad = edad 

        #Metodo para imprimir los datos del perro 
def imprimirDatos(self):
            print("Nombre: ", self.nombre)
            print("Raza: ", self.raza )
            print("Edad: ", self.edad)
            print("Especie: ", self.especie)

def main(): 
    #Crear un objeto de la clase de perro 
    perro1 = Perro("Firulais", "Labtador", 5)
    perro1.imprimirDatos()
    perro2 = Perro("Rex", "Pastor Aleman", 3)
    perro2.imprimirDatos()
    print("Informacion del perro 2: ", perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Max", "Bulldog", 2)
    perro3.imprimirDatos()
    perro4 = Perro("Dante")
    perro4.edad = 4 
    perro4.imprimirDatos()
    perro2.raza = "Pastor Belga"
    perro2.imprimirDatos 
    perro5 = Perro("Raya", "Siames", 1)
    perro5.especie = "Felis catus"
    perro5.imprimirDatos()

    if __name__ == "__main__": 
        main()