class ave:
    def __init__(self, color = "verde"):
        self.color = color

    def volar(self):
        print("puedo volar")

class canario(ave):
    def __init__(self, nombre, color):
        super().__init__(color)
        self.nombre = nombre

    def info(self):
        pass

canario = canario("amarillo", "fulanito")
print(canario.color)