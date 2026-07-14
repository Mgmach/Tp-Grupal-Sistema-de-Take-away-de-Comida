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
                # case "Restaurante":
                # iniciar_menu_restaurante(usuario_logueado)  #Inicia Menu del Rol Restaurante
                # case "Administrador":
                # iniciar_menu_admin(usuario_logueado)        #Inicia Menu del Rol administrador

def iniciar_menu_cliente(cliente:dict) -> None:
    while True:
        mostrar_menu_cliente()
        eleccion = elegir_menu(3)
        match eleccion:
            case 1:
                ver_datos(cliente)
            case 2:
                realizar_pedido(cliente)
            case 3:    
                print("Saliendo del sistema...")
                break
                    
        input("\nPresione Enter para continuar...")