class Cafetera:
    def preparar_cafe(self):
        self._hervir_agua()
        self._moler_cafe()
        print("Cafe listo!")

    def _hervir_agua(self):
        print("Hirviendo el agua")

    def _moler_cafe(self):
        print("Moliendo cafe")

def main():
    cafetera = Cafetera()
    cafetera.preparar_cafe()

    if __name__ == "__main__":
        main()