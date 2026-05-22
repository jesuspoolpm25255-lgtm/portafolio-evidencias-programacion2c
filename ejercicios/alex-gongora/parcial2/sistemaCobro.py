# ===================================================
# PROGRAMA: Sistema de Cobro v1.0 - Versión Modular
# AUTOR: [Tu nombre]
# DESCRIPCIÓN: Calcula el total de una venta aplicando
# descuento del 10% si supera $1000 y agrega IVA del 16%
# ===================================================

def pedir_datos_producto():
    """
    Función: pedir_datos_producto
    Descripción: Solicita al usuario los datos del producto a cobrar.
    Parámetros: No recibe parámetros.
    Retorna: 
        producto (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de productos.
    """
    print("--- Sistema de Cobro v1.0 ---")
    producto = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return producto, precio, cantidad

def calcular_subtotal(precio, cantidad):
    """
    Función: calcular_subtotal
    Descripción: Calcula el importe base multiplicando precio por cantidad.
    Parámetros:
        precio (float): Precio unitario del producto.
        cantidad (int): Número de unidades vendidas.
    Retorna:
        float: Resultado de precio * cantidad.
    """
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal):
    """
    Función: calcular_descuento
    Descripción: Aplica un descuento del 10% si el subtotal es mayor a $1000.
    Parámetros:
        subtotal (float): Monto antes de impuestos y descuentos.
    Retorna:
        float: Monto del descuento aplicado. Devuelve 0 si no aplica.
    """
    if subtotal > 1000:
        descuento = subtotal * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    else:
        return 0

def calcular_iva(subtotal_con_descuento):
    """
    Función: calcular_iva
    Descripción: Calcula el IVA del 16% sobre el monto con descuento aplicado.
    Parámetros:
        subtotal_con_descuento (float): Subtotal después de restar el descuento.
    Retorna:
        float: Monto correspondiente al 16% de IVA.
    """
    iva = subtotal_con_descuento * 0.16
    return iva

def calcular_total_final(subtotal_con_descuento, iva):
    """
    Función: calcular_total_final
    Descripción: Obtiene el total a pagar sumando el subtotal con descuento + IVA.
    Parámetros:
        subtotal_con_descuento (float): Monto ya con descuento aplicado.
        iva (float): Monto del impuesto calculado.
    Retorna:
        float: Total final que debe pagar el cliente.
    """
    total = subtotal_con_descuento + iva
    return total

def imprimir_ticket(producto, subtotal, iva, total_final):
    """
    Función: imprimir_ticket
    Descripción: Muestra en pantalla el resumen de la venta en formato ticket.
    Parámetros:
        producto (str): Nombre del producto vendido.
        subtotal (float): Subtotal después del descuento.
        iva (float): Monto del IVA.
        total_final (float): Total a pagar.
    Retorna: No retorna valores. Solo imprime en consola.
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("------------------------")

def main():
    """
    Función: main
    Descripción: Función principal que controla el flujo del programa.
    Coordina la llamada a todas las demás funciones en orden lógico.
    """
    producto, precio, cantidad = pedir_datos_producto()
    
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    
    subtotal_con_descuento = subtotal - descuento
    iva = calcular_iva(subtotal_con_descuento)
    total_final = calcular_total_final(subtotal_con_descuento, iva)
    
    imprimir_ticket(producto, subtotal_con_descuento, iva, total_final)

# Punto de entrada del programa 24
if __name__ == "__main__":
    main()
