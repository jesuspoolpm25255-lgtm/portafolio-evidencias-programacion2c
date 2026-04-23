#Jesus pool
def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal de una compra multiplicando precio por cantidad.
    """
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal, porcentaje_descuento):
    """
    Calcula el monto en dinero que se descuenta del subtotal.
    """
    descuento = subtotal * porcentaje_descuento / 100
    return descuento

def subtotal_con_descuento(subtotal, descuento):
    """
    Resta el monto del descuento al subtotal original.
    """
    subtotal_descontado = subtotal - descuento
    return subtotal_descontado

def calcular_iva(subtotal_descontado, porcentaje_iva):
    """
    Calcula el monto del IVA sobre el subtotal con descuento.
    """
    iva = subtotal_descontado * porcentaje_iva / 100
    return iva

def calcular_total(subtotal_descontado, iva):
    """
    Calcula el total final sumando el subtotal con descuento más el IVA.
    """
    total = subtotal_descontado + iva
    return total

def mostrar_ticket(precio, cantidad, desc_porc, iva_porc):
    """
    Orquesta todas las funciones de cálculo e imprime el ticket de compra.
    """
    sub = calcular_subtotal(precio, cantidad)
    desc_monto = calcular_descuento(sub, desc_porc)
    sub_desc = subtotal_con_descuento(sub, desc_monto)
    iva_monto = calcular_iva(sub_desc, iva_porc)
    total_final = calcular_total(sub_desc, iva_monto)
    
    print("\n--- TICKET DE COMPRA ---")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${sub}")
    print(f"Descuento {desc_porc}%: -${desc_monto}")
    print(f"Subtotal con descuento: ${sub_desc}")
    print(f"IVA {iva_porc}%: +${iva_monto}")
    print(f"TOTAL A PAGAR: ${total_final}")
    print("------------------------\n")

def menu():
    while True:
        print("=== MENÚ SISTEMA DE COBRO ===")
        print("1. Calcular nuevo ticket")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                precio = float(input("Ingresa el precio del producto: $"))
                cantidad = int(input("Ingresa la cantidad: "))
                desc = float(input("Ingresa el % de descuento: "))
                iva = float(input("Ingresa el % de IVA: "))
                
                mostrar_ticket(precio, cantidad, desc, iva)
                
            except ValueError:
                print("Error: Ingresa solo números. Intenta de nuevo.\n")
                
        elif opcion == "2":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción inválida. Elige 1 o 2.\n")

# Iniciar el programa
menu()