from Input import *
from Funciones import *

def mostrar_menu_inicio() -> None:
    """Muestra el menu principal con todas las opciones disponibles.
    """
    print("=" * 60)
    print("=== Bienvenido al sistema de delivery UTN Eats ===")
    print("Pide desde la comodidad de tu casa")
    print("Este sistema te permite realizar pedidos de comida entre clientes y restaurantes.")
    print(" " * 15 + "Seleccione una opcion:")
    print("=" * 60)
    print("1) Iniciar Sesión")
    print("2) Salir")
    print("=" * 60)

def mostrar_menu_cliente() -> None:
    """Muestra el menu principal con todas las opciones disponibles.
    """
    print("=" * 60)
    print(" " * 15 + "Seleccione una opcion:")
    print("=" * 60)
    print("1) Ver datos")
    print("2) Realizar pedido (Simulado)")
    print("3) Salir")
    print("=" * 60)

def ver_datos(usuario:dict) -> None:
    """Muestra todos los datos del usuario, excepto la contraseña."""
    for clave, valor in usuario.items():
        if clave != "contrasena":
            print(f"{clave}: {valor}")

def mostrar_menu_comidas(comidas:dict) -> None:
    """Muestra las opciones de comida disponibles."""
    print("=== Menú de Comidas ===")
    for clave, producto in comidas.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']}")

def mostrar_menu_bebidas(bebidas:dict) -> None:
    """Muestra las opciones de bebida disponibles."""
    print("=== Menú de Bebidas ===")
    for clave, producto in bebidas.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']}")

def mostrar_menu_restaurante() -> None:
    """Muestra el menu principal con todas las opciones disponibles.
    """
    print("=" * 60)
    print("=== Bienvenido al sistema de delivery UTN Eats ===")
    print("Pide desde la comodidad de tu casa")
    print("Este sistema te permite realizar pedidos de comida entre clientes y restaurantes.")
    print(" " * 15 + "Seleccione una opcion:")
    print("=" * 60)
    print(" Iniciar Sesión")
    print("=" * 60)

def mostrar_menu_administrador() -> None:
    """Muestra el menu principal con todas las opciones disponibles.
    """
    print("=" * 60)
    print("=== Bienvenido al sistema de delivery UTN Eats ===")
    print("Pide desde la comodidad de tu casa")
    print("Este sistema te permite realizar pedidos de comida entre clientes y restaurantes.")
    print(" " * 15 + "Seleccione una opcion:")
    print("=" * 60)
    print(" Iniciar Sesión")
    print("=" * 60)




def obtener_texto_estado(estado: int) -> str:
    """
    Muestra el estado de un pedido a un texto legible para
    mostrar en pantalla
 
    Args:
        estado (int): Estado del pedido
 
    Returns:
        str: "Pendiente", "En preparación" o "Entregado"
    """
    if estado == 1:
        texto = "Pendiente"
    elif estado == 2:
        texto = "En preparación"
    else:
        texto = "Entregado"
 
    return texto



def imprimir_ticket_pedido(items_pedido: list, total: float) -> None:
    """
    Muestra el ticket de los productos elegidos junto con el
    total antes de que se confirme el pedido
 
    Args:
        items_pedido (list): Lista de diccionarios con los productos
            elegidos
        total (float): Total calculado del pedido
 
    Returns:
        None
    """
    print("\n----- RESUMEN DEL PEDIDO -----")
    for i in range(len(items_pedido)):
        item = items_pedido[i]
        subtotal = item["precio"] * item["cantidad"]
        print(f"{item['cantidad']} x {item['nombre']} - ${subtotal}")
    print("-" * 30)
    print(f"TOTAL: ${total}")



def imprimir_pedido(pedido: dict) -> None:
    """
    Muestra los datos de un pedido puntual
 
    Args:
        pedido (dict): Diccionario con los datos del pedido
 
    Returns:
        None
    """
    print("-" * 40)
    print(f"Número de pedido : {pedido['numero']}")
    print(f"Restaurante      : {pedido['restaurante']}")
    print(f"Total            : ${pedido['total']}")
    print(f"Estado           : {obtener_texto_estado(pedido['estado'])}")
    print("-" * 40)
