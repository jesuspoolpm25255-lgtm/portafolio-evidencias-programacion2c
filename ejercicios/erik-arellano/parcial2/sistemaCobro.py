<<<<<<< HEAD
 # --- FUNCION 1: Pedir datos al usuario ---
def capturar_datos():
    """
    Solicita al usuario los datos del producto.

    Retorno:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades.
    """
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad

# --- FUNCION 2: Calcular el subtotal ---
def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal multiplicando el precio por la cantidad.

    Argumentos:
        precio (float): Precio unitario.
        cantidad (int): Número de unidades.

    Retorno:
        float: Resultado de la multiplicación.
    """
    return precio * cantidad

# --- FUNCION 3: Aplicar descuento ---
def aplicar_descuento(monto):
    """
    Aplica un descuento del 10% si el monto es mayor a $1000.

    Argumentos:
        monto (float): El subtotal de la compra.

    Retorno:
        float: Valor del descuento a restar.
    """
    if monto > 1000:
        descuento = monto * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    else:
        return 0

# --- FUNCION 4: Calcular IVA ---
def calcular_iva(monto):
    """
    Calcula el impuesto IVA del 16%.

    Argumentos:
        monto (float): Monto sobre el cual calcular el impuesto.

    Retorno:
        float: Valor del IVA calculado.
    """
    return monto * 0.16

# --- FUNCION 5: Imprimir el ticket ---
def mostrar_ticket(producto, sub, desc, iva, total):
    """
    Muestra en pantalla el ticket de venta formateado.

    Argumentos:
        producto (str): Nombre del artículo.
        sub (float): Monto del subtotal.
        desc (float): Monto del descuento.
        iva (float): Monto del impuesto.
        total (float): Monto final a pagar.
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${sub:.2f}")
    print(f"Descuento: -${desc:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("------------------------")

# ==============================================
#              PROGRAMA PRINCIPAL
# ==============================================

print("--- Sistema de Cobro v1.0 ---")

# Llamamos a las funciones en orden
producto, precio, cantidad = capturar_datos()

subtotal = calcular_subtotal(precio, cantidad)
descuento = aplicar_descuento(subtotal)
subtotal_con_desc = subtotal - descuento
iva = calcular_iva(subtotal_con_desc)
total_final = subtotal_con_desc + iva

mostrar_ticket(producto, subtotal, descuento, iva, total_final)
=======
# Función para calcular el subtotal
def calcular_subtotal(precio, cantidad):
    """Calcula el subtotal multiplicando precio por cantidad"""
    return precio * cantidad


# Función para calcular el descuento
def calcular_descuento(subtotal):
    """Aplica un 10% de descuento si el subtotal es mayor a 1000"""
    if subtotal > 1000:
        return subtotal * 0.10
    return 0


# Función para calcular el IVA
def calcular_iva(subtotal_con_descuento):
    """Calcula el IVA del 16%"""
    return subtotal_con_descuento * 0.16


# Función para calcular el total final
def calcular_total(subtotal_con_descuento, iva):
    """Suma subtotal con descuento más IVA"""
    return subtotal_con_descuento + iva


# Función para imprimir el ticket
def imprimir_ticket(producto, subtotal, descuento, iva, total):
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------")


# Función principal
def main():
    print("--- Sistema de Cobro v1.0 ---")

    try:
        producto = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad: "))

        if precio < 0 or cantidad < 0:
            print("Error: precio y cantidad deben ser positivos.")
            return

        subtotal = calcular_subtotal(precio, cantidad)
        descuento = calcular_descuento(subtotal)
        subtotal_con_descuento = subtotal - descuento
        iva = calcular_iva(subtotal_con_descuento)
        total = calcular_total(subtotal_con_descuento, iva)

        imprimir_ticket(producto, subtotal, descuento, iva, total)

    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
>>>>>>> df8f038e44a3b99e95e466dc87fba1ad8937cc9c
