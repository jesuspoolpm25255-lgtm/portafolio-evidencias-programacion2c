class Ave:
    def _init_(self, color = "Verede"):
        self.color = color

    def voalr(self):
        print("Puedo volar")

class Canario(Ave):
    def _init_(self, color, nombre):
        super()._init_(color)
        self.nombre = nombre

    def informacion(self):
        pass

canario = Canario("Amarillo","fulanito")
print(canario.color)
canario.volar()
print(canario.color)