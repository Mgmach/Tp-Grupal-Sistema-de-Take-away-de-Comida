from Input import *
from Funciones import *
from Prints import *

def elegir_menu(max:int) -> int:
    """Solicita al usuario que elija una opcion del menu y la valida.
    """
    num = ingresar_entero_rango(
        "Elija una opcion: ",
        "Error, debe elegir una opcion valida",
        maximo = max
    )
    return num

def iniciar_menu():
    while True:
        mostrar_menu_inicio()
        usuario_logueado = iniciar_sesion()
        if usuario_logueado is None:
            print("Usuario o contraseña incorrectos.")
        else:
            match usuario_logueado["tipo"]:
                case "Cliente":
                    iniciar_menu_cliente(usuario_logueado)
                case "Restaurante":
                    iniciar_menu_restaurante(usuario_logueado)  #Inicia Menu del Rol Restaurante
                case "Administrador":
                    iniciar_menu_admin(usuario_logueado)        #Inicia Menu del Rol administrador

def iniciar_menu_cliente(cliente:dict) -> None:
    """Menú del rol Cliente"""
    while True:
        mostrar_menu_cliente()
        eleccion = elegir_menu(3)
        match eleccion:
            case 1:
                ver_datos(cliente)
            case 2:
                realizar_pedido(cliente)
            case 3:    
                print("Saliendo...")
                break
                    
        input("\nPresione Enter para continuar...")

    
def iniciar_menu_restaurante(restaurante: dict) -> None:
    while True:
        mostrar_menu_restaurante()
        eleccion = elegir_menu(5)

        match eleccion:
            case 1:
                ver_datos(restaurante)
            case 2:
                preparar_pedido()
            case 3:
                # entregar pedido
            case 4:
                # ver la facturacion del restaurante
            case 5:    
                print("Saliendo...")
                break

        input("\nPresione Enter para continuar...")

def iniciar_menu_admin(admin: dict) -> None:
    """Menú del rol Administrador"""
    while True:
        mostrar_menu_administrador()
        eleccion = elegir_menu(4)

        match eleccion:
            case 1:
                # crear usuario 
            case 2:
                # borrar usuario 
            case 3:
                # ver la info de sistema
            case 4:
                print("Saliendo...")
                break
