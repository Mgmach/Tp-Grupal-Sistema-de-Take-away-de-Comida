from Input import *
from Prints import *
from Usuarios import *
from Productos import *

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
        print("Pedido Canselado.") 