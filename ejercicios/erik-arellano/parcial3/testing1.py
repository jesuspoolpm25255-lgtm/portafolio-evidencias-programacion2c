def calcular_media(*args):
   """
   Devuelve el valor de la media o promedio de un conjuntos de datos numericos


   Args:
    *args (int): un numero variable de argumentos que representas los datos
    Returns:
    (float): el valor de los de los datos


   """
   return(sum(*args)/len(*args))


assert(calcular_media([3,5,4]) == 4.0)
assert(calcular_media([10,10,30]) == 20.0)
assert(calcular_media([3,4,5]) ==2.0)

