from Input import *
from Prints import *
from Usuarios import *
from Productos import *
import json
import os
import random

def agregar_elemento(elemento:any, lista:list) -> list:
    """Agrega un elemento al final de una lista (equivalente a append).
    Args:
        lista (list): lista a la que se agregará el elemento.
        elemento (any): elemento a agregar.
    Returns:
        list: lista con el elemento agregado.
    """
    lista[len(lista):] = [elemento]
    return lista

def iniciar_sesion():
    usuario_ingresado = pedir_nombre("Ingresar usuario: ", 4)
    contrasena_ingresada = pedir_contraseña("Ingresar contraseña: ")

    for u in usuarios:
        if u["usuario"] == usuario_ingresado and u["contrasena"] == contrasena_ingresada:
            return u
    return None

def preparar_pedido() -> None:
    """
    Simula la preparación de un pedido generando un número
    aleatorio de exactamente 13 cifras
    """
    numero = random.randint(1000000000000, 9999999999999)
    print(f"\n  Pedido en preparacion.")
    print(f"  Numero de pedido: {numero}")

def realizar_pedido():
    restaurante = pedir_nombre("Ingresar Restaurante; ", 3)
    mostrar_menu_comidas(comidas)
    num_comida = ingresar_entero_rango(
        "Elija un producto: ",
        "Error, debe elegir un producto correcto",
        maximo = 5
    )
    cantidad_comida = ingresar_entero_rango(
        "Cuanto desea ordenar?",
        "Error, debe elegir menos de 15",
        maximo = 15
    )

    mostrar_menu_bebidas(bebidas)
    num_bebida = ingresar_entero_rango(
        "Elija un producto: ",
        "Error, debe elegir un producto correcto",
        maximo = 5
    )
    if num_bebida == 0:
        cantidad_bebida = ingresar_entero_rango(
            "Cuanto desea ordenar?",
            "Error, debe elegir menos de 15",
            maximo = 15
        )
    total_compra = (comidas[num_comida]["precio"] * cantidad_comida) + (bebidas[num_bebida]["precio"] * cantidad_bebida)
    confirmacion = input(f"Su total es de {total_compra}$ desea confirmar? (y/n)")
    if confirmacion == "y":
        print(f"Gracias por comprar en {restaurante}")
    else:
        print("Pedido Cancelado.") 



def buscar_usuario(lista_usuarios: list, nombre_usuario: str) -> dict:
    """
    Busca un usuario dentro de la lista de usuarios por su nombre
 
    Args:
        lista_usuarios (list): Lista de diccionarios con los usuarios
        nombre_usuario (str): Nombre de usuario a buscar
 
    Returns:
        dict: Diccionario del usuario si lo encuentra
        None si no existe
    """

    usuario_encontrado = None
 
    for i in range(len(lista_usuarios)):
        if lista_usuarios[i]["usuario"] == nombre_usuario:
            usuario_encontrado = lista_usuarios[i]
            break
 
    return usuario_encontrado
 
 
def verificar_credenciales(usuario_dict: dict, contraseña: str) -> bool:
    """
    Verifica si la contraseña ingresada coincide con la del usuario recibido
 
    Args:
        usuario_dict (dict): Diccionario del usuario a verificar
        contrasena (str): Contraseña ingresada por el usuario
 
    Returns:
        bool: True si la contraseña coincide
        False en caso contrario
    """

    retorno = False
 
    if usuario_dict["contraseña"] == contraseña:
        retorno = True
 
    return retorno
 
 
def buscar_usuario_por_login(lista_usuarios: list, nombre_usuario: str, contraseña: str) -> dict:
    """
    Busca dentro de la lista de usuarios un nombre de usuario y
    contraseña que coincidan con los ingresados
 
    Args:
        lista_usuarios (list): Lista de diccionarios con los usuarios
        nombre_usuario (str): Nombre de usuario ingresado
        contrasena (str): Contraseña ingresada
 
    Returns:
        dict: Diccionario del usuario si las credenciales son correctas
        None si no existe el usuario o la contraseña no coincide
    """

    usuario_encontrado = buscar_usuario(lista_usuarios, nombre_usuario)
    resultado = None
 
    if usuario_encontrado != None:
        if verificar_credenciales(usuario_encontrado, contraseña) == True:
            resultado = usuario_encontrado
 
    return resultado


def filtrar_catalogo(catalogo: list, nombre_restaurante: str) -> list:
    """
    Filtra el catálogo completo de productos y devuelve
    solamente los que pertenecen al restaurante indicado
 
    Args:
        catalogo (list): Lista de diccionarios con todos los productos
            del sistema
        nombre_restaurante (str): Nombre del restaurante a filtrar
 
    Returns:
        list: Lista de productos que pertenecen a ese restaurante
    """
    productos_filtrados = []
 
    for i in range(len(catalogo)):
        if catalogo[i]["restaurante"] == nombre_restaurante:
            productos_filtrados.append(catalogo[i])
 
    return productos_filtrados

def calcular_total_pedido(items_pedido: list) -> float:
    """
    Calcula el total de un pedido sumando el precio de
    cada producto elegido, multiplicado por su cantidad
 
    Args:
        items_pedido (list): Lista de diccionarios, cada uno con al
            menos las claves "precio" y "cantidad"
 
    Returns:
        float: Total del pedido
    """
    total = 0
 
    for i in range(len(items_pedido)):
        total += items_pedido[i]["precio"] * items_pedido[i]["cantidad"]
 
    return total


def obtener_pedidos_a_matriz(pedidos: list) -> list:
    """
    Transforma la lista de pedidos en una matriz donde
    cada fila representa un pedido con su número
    su total y su estado
 
    Args:
        pedidos (list): Lista de diccionarios con los pedidos
 
    Returns:
        list: Matriz 
    """
    matriz = []
 
    for i in range(len(pedidos)):
        fila = [pedidos[i]["numero"], pedidos[i]["total"], pedidos[i]["estado"]]
        matriz.append(fila)
 
    return matriz



def cargar_pedidos(ruta: str) -> list:
    """
    Lee la lista de pedidos desde un archivo JSON
 
    Args:
        ruta (str): Ruta del archivo JSON
 
    Returns:
        list: Lista de pedidos
        Lista vacía si el archivo no existe
    """
    pedidos = []
 
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            pedidos = json.load(archivo)
    else:
        print(f"No se encontró el archivo {ruta}")
 
    return pedidos
 
