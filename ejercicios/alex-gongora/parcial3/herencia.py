class Ave:
    def __init__(self, color = "verde"):
        self.color = color

    def volar(self):
        print("Puedo volar")

class Canario(Ave):
    def __init__(self,color, nombre):
        super().__init__(color)
        self.nombre = nombre

    def informacion(self):
        pass

canario = Canario("Amarillo", "Fulanito")
print(canario.color)