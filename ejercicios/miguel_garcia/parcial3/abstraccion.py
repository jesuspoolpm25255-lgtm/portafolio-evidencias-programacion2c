class Cafetera:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler_cafe()
        print("Café listo!")

    def __hervir_agua(self):
        print("Hirviendo el agua")

    def __moler_cafe(self):
        print("Moliendo café")

def main():
    cafetera = Cafetera()
    cafetera.preparar_cafe()

if __name__ == "__main__":
    main()