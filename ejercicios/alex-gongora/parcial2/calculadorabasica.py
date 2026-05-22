#Funciones basicas
def suma(a,b):
    result = a + b
    return result

def resta(a,b):
    result = a - b

def multi(b,a):
    result= b * a
    return result

def div(a,b):
    return a / b

#Menu de opciones
opcion = 0
while(opcion != 5):
    print("---- Menu de opciones ----")
    print("1. Sumar 2 valores")
    print("2. Restas 2 valores")
    print("3. Multiplicar 2 numeros")
    print("4. Dividir 2 numeros")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #Suma de dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("ingresa el segundo valor a sumar: "))
        print(f"Resultado de la suma: {suma(n1,n2)}")

    elif opcion == 2: 
        #Resta de dos numeros
        n1 = float(input("\nIngresa el minuendo: "))
        n2 = float(input("\nIngresa el sustraendo: "))
        print(f"Cociente de la resta: {resta(n1,n2)}")

    elif opcion == 3:
        #Multiplicacion de dos numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n2 = float(input("\nIngresa el segundo factor: "))
        print(f"producto resultante: {multi(n1,n2)}")

    elif opcion == 4: 
         #division de dos numeros
        n1 = float(input("\nIngresa el dividiendo: "))
        n2 = float(input("\nIngresa el divisor: "))
        print(f"cociente resultante: {div(n1,n2)}")

    elif opcion == 5:   
        #finalizacion del programa
        print("progrma finalizado. . .") 
    else:
        #mensaje de error por opcion no valida
        print("Programa seleccionada no valida, intente de nuevo!")