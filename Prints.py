from Input import *
from Funciones import *

def mostrar_menu_inicio() -> None:
    """Muestra el menu principal con todas las opciones disponibles.
    """
    print("=" * 60)
    print(" " * 15 + "Seleccione una opcion:")
    print("=" * 60)
    print(" 1) Cargar datos de alumnos.")
    print(" 2) Mostrar egresados por plan.")
    print(" 3) Mostrar egresados anteriores al año 2000")
    print(" 4) Buscar alumno por nombre o apellido")
    print(" 5) Salón de la fama: alumnos con promedio mayor o igual a 9")
    print(" 6) Salir del sistema.")
    print("=" * 60)

def imprimir_alumno(alumno:list) -> None:
    """Muestra los datos de un alumno.
    Args:
        lista_alumnos (list): lista de alumnos a mostrar.
    """
    print("-" * 45)
    print(f"  Legajo     : {alumno['legajo']}")
    print(f"  Nombre     : {alumno['nombre']} {alumno['apellido']}")
    print(f"  Año egreso : {alumno['egreso']}")
    print(f"  Plan       : {alumno['plan']}")
    print(f"  Promedio   : {alumno['nota_promedio']}")
    print("-" * 45)

def imprimir_lista_alumnos(lista_alumnos:list, mensaje:str = "No hay alumnos para mostrar.") -> None:
    """Muestra todos los alumnos de una lista, uno por uno, reutilizando imprimir_alumno(). Si la lista está vacía, avisa.
    Args:
        lista_alumnos (list): lista de alumnos a mostrar.
    """
    if len(lista_alumnos) == 0:
        print(mensaje)
    else:
        print(f"\n  Total de alumnos: {len(lista_alumnos)}\n")
        for i in range(len(lista_alumnos)):
            imprimir_alumno(lista_alumnos[i])
          
