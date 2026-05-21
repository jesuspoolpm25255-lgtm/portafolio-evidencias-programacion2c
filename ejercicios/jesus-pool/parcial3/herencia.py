class Ave:
    def __init__(self, color="verde"):
        self.color = color

    def volar(self):
        print("Puedo volar")


class Canario(Ave):
    def informacion(self):
        pass


fulanito = Canario()
print(fulanito.color)

fulanito.volar()

fulanito.color = "Amarillo"

print(fulanito.color)
