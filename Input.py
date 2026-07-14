def verificar_cadena_entera(cadena:str) -> bool:
    """Verifica si una cadena representa un número entero válido.
    Args:
        cadena (str): cadena a verificar.
    Returns:
        bool: True si la cadena es un entero válido, False en caso contrario.
    """
    if len(cadena) > 0 and cadena != "-":
        bandera_entero = True
        for i in range(len(cadena)):
            caracter = cadena[i]
            ascii_caracter = ord(caracter)
            if ascii_caracter > 57 or ascii_caracter < 48 and (i != 0 or caracter != "-"):
                bandera_entero = False
                break
    else:
        bandera_entero = False
    
    return bandera_entero

def ingresar_entero(mensaje:str, mensaje_error:str="Error, Debe ingresar un numero entero") -> int:
    """Solicita al usuario un número entero y lo valida.
    Args:
        mensaje (str): mensaje a mostrar al usuario.
        mensaje_error (str): mensaje a mostrar si el dato ingresado no es válido.
    Returns:
        int: número entero ingresado por el usuario.
    """
    numero_entero = input(mensaje)
    while not verificar_cadena_entera(numero_entero):
        print(mensaje_error)
        numero_entero = input(mensaje)
    
    numero_entero = int(numero_entero)

    return numero_entero

def ingresar_entero_rango(mensaje:str, mensaje_error:str, maximo:int, minimo:int=0) -> int:
    """Solicita al usuario un número entero dentro de un rango y lo valida.
    Args:
        mensaje (str): mensaje a mostrar al usuario.
        mensaje_error (str): mensaje a mostrar si el dato ingresado no es válido.
        minimo (int): valor mínimo aceptado.
        maximo (int): valor máximo aceptado.
    Returns:
        int: número entero ingresado por el usuario dentro del rango.
    """
    numero_entero = ingresar_entero(mensaje)
    while numero_entero <= minimo or numero_entero >= maximo:
        print(mensaje_error)
        numero_entero = ingresar_entero(mensaje)

    return numero_entero

def es_flotante(cadena:str) -> bool:
    """Verifica si una cadena representa un número flotante válido
    (un único punto decimal, dígitos antes y después).
    Args:
        cadena (str): cadena a verificar.
    Returns:
        bool: True si la cadena es un flotante válido, False en caso contrario.
    """
    if len(cadena) == 0:
        return False

    punto_encontrado = False
    inicio = 0

    if cadena[0] == "-":
        inicio = 1

    if inicio == len(cadena):
        return False

    for i in range(inicio, len(cadena)):
        caracter = cadena[i]
        if caracter == ".":
            if punto_encontrado:
                return False  
            punto_encontrado = True
        else:
            codigo = ord(caracter)
            if codigo < 48 or codigo > 57:
                return False 

    return True

def ingresar_flotante(mensaje:str, mensaje_error:str="Error, debe ingresar un número decimal") -> float:
    """Solicita al usuario un número flotante y lo valida.
    Args:
        mensaje (str): mensaje a mostrar al usuario.
        mensaje_error (str): mensaje a mostrar si el dato ingresado no es válido.
    Returns:
        float: número flotante ingresado por el usuario.
    """
    numero = input(mensaje)
    while not es_flotante(numero):
        print(mensaje_error)
        numero = input(mensaje)
    return float(numero)

def ingresar_flotante_rango(mensaje:str, mensaje_error:str, minimo:int, maximo:int) -> float:
    """Solicita al usuario un número flotante dentro de un rango y lo valida.
    Args:
        mensaje (str): mensaje a mostrar al usuario.
        mensaje_error (str): mensaje a mostrar si el dato ingresado no es válido.
        minimo (int): valor mínimo aceptado.
        maximo (int): valor máximo aceptado.
    Returns:
        float: número flotante ingresado por el usuario dentro del rango.
    """
    numero = ingresar_flotante(mensaje)
    while numero <= minimo or numero > maximo:
        print(mensaje_error)
        numero = ingresar_flotante(mensaje)
    return numero

def ingresar_cadena(mensaje:str, mensaje_error:str="Debe Ingresar un Dato valido.") -> str:
    """Solicita al usuario una cadena no vacía y la valida.
    Args:
        mensaje (str): mensaje a mostrar al usuario.
        mensaje_error (str): mensaje a mostrar si el dato ingresado no es válido.
    Returns:
        str: cadena ingresada por el usuario.
    """
    cadena = input(mensaje)
    while len(cadena) == 0:
        print(mensaje_error)
        cadena = input(mensaje)
    return cadena

def es_letra(caracter:str) -> bool:
    """Verifica si un carácter es una letra (a-z, A-Z) o un espacio.
    Args:
        caracter (str): carácter a verificar.
    Returns:
        bool: True si el carácter es una letra o espacio, False en caso contrario.
    """
    codigo = ord(caracter)
    return (65 <= codigo <= 90) or (97 <= codigo <= 122) or codigo == 32

def es_nombre_valido(cadena:str, minimo:int) -> bool:
    """Valida que la cadena tenga al menos un minimo de caracteres y sean solo letras/espacios.
    Args:
        cadena (str): cadena a validar.
    Returns:
        bool: True si la cadena es un nombre válido, False en caso contrario.
    """
    valido = len(cadena) >= minimo
    if valido:
        for i in range(len(cadena)):
            if not es_letra(cadena[i]):
                valido = False
                break
    return valido

def pedir_nombre(mensaje:str, minimo:int) -> str:
    """Solicita al usuario un nombre o apellido y lo valida
    (mínimo caracteres, solo letras y espacios).
    Args:
        mensaje (str): mensaje a mostrar al usuario.
    Returns:
        str: nombre o apellido ingresado por el usuario.
    """
    dato = ingresar_cadena(mensaje)
    while not es_nombre_valido(dato):
        print(f"  Error: debe ingresar al menos {minimo} letras, sin números ni símbolos.")
        dato = ingresar_cadena(mensaje)
    return dato

def pedir_contraseña(mensaje:str) -> str:
    cadena = ingresar_cadena(mensaje)
    if len(cadena) <= 8:
        print("Error, la contraseña debe ser mayor a 8 caracteres.")
        cadena = ingresar_cadena(mensaje)
    return cadena

def pedir_tipo_usuario(mensaje:str, nuevo_usuario:bool) ->str:
    while True:
        print(mensaje)
        print("1. Cliente")
        print("2. Restaurante")
        if not nuevo_usuario:
            print("3. Administrador")
        opcion = input("Ingrese una opción (Numero): ")

        match opcion:
            case 1:
                return "Cliente"
            case 2:
                return "Restaurante"
            case 3:
                return "Administrador"
            case _:
                print("Opción inválida. Intente nuevamente.\n")