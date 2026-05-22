class Perro:
    
    def __init__ (self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def imprimirDatos(self):
            print("Nombre: ", self.nombre)
            print("Raza: ", self.raza)
            print("Edad: ", self.edad)

def main():
    #crear
    perro1 = Perro("firulais","labrador",5)
    perro1.imprimirDatos()
    perro2 = Perro("rex ", "pasor aleman",3)
    perro2.imprimirDatos()
    print("informacion perro 2: "),perro2.nombre, perro2.raza, perro2.edad 
    perro3 = Perro("max" , "bulldog",2)
    perro3.imprimirDatos()
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "pator Delga"
    perro2.imprimirDatos              
    perro5 = Perro("Raya", "siames" ,1)
    perro5.especie = "Falis catus"
    perro5.imprimirDatos
if __name__== "__main__":
     main()