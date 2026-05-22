def formato_nombre(name,lastName):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.

    Argumentos:
           name (str): Primer nombre del usuario
           lastName (str): Apellido paterno del usuario.

    Retorno:
        (str): El nobre completo en formato Apellido, Nombre.
    """
    return f"{lastName}, {name}"

#Funcion main para ejecucion del codigo. 
def main():
    _name= input("Introduce tu primer apellido: ")
_lastName = input("Introduce tu apellido paterno: ")
print(formato_nombre(__name__,_lastName))

if __name__ == "__main__":
    main()