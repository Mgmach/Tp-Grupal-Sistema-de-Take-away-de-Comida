from Input import *
from Funciones import *
from Prints import *

def elegir_menu() -> int:
    """Solicita al usuario que elija una opcion del menu y la valida.
    """
    num = ingresar_entero_rango(
        "Elija una opcion: ",
        "Error, debe elegir una opcion valida",
        maximo=6
    )
    return num

def iniciar_menu() -> None:
    """Inicia el loop principal del menu, controla el flujo del programa
    y llama a las funciones correspondientes segun la opcion elegida.
    Impide el acceso a opciones que requieren datos cargados previamente.
    """    
    lista_alumnos = []
    datos_cargados = False
    es_manual = False

    while True:
        mostrar_menu_inicio()
        eleccion = elegir_menu()

        if eleccion == 13:
            print("Saliendo del sistema...")
            break

        if eleccion != 1 and not datos_cargados:
            print("Primero debe cargar los datos de los alumnos.")
        else:
            match eleccion:
                case 1:
                    lista_alumnos, es_manual = elejir_carga(lista_alumnos)
                    datos_cargados = True
                case 2:
                    imprimir_lista_alumnos(buscar_por_plan(lista_alumnos))
                case 3:
                    imprimir_lista_alumnos(buscar_egresados_anteriores_a(lista_alumnos, 2000))
                case 4:
                    imprimir_lista_alumnos(buscar_por_nombre_apellido(lista_alumnos))
                case 5:
                    imprimir_lista_alumnos(buscar_mejores_promedios(lista_alumnos))
                case 6:
                    guardar_json("alumnos.json", lista_alumnos)
                    print("Datos guardados correctamente.")
                    print("Saliendo del sistema...")
                    break
                    
        input("\nPresione Enter para continuar...")