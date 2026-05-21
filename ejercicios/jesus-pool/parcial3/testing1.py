def calcular_media(*args):
    """Devuelve el valor de la media o promedio de datos numericos
    Args:
        *args (int): Un numero variable de argumentos que representan los datos numericos
    Return:
        (float): El valor de la media o promedio de los datos numericos
    """

    return (sum(*args)/len(*args))

assert(calcular_media([3,5,4]) == 4.0)
assert(calcular_media([10,20,30]) == 20.0)