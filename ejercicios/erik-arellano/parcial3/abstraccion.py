class Cafetera:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler_cafe()
        print("Cafe listo!")

    def __hervir_agua(self):
        print("Hirviendo el agua")

    def __moler_cafe(self):
        print("Moleindo cafe")

def main():
    cafetera = cafetera()
    cafetera.preparar_cafe()

if __name__ == "_main_":
   main()