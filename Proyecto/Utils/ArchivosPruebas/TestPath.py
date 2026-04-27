# Crea Carpetas, y las elimina luego de 5 segundos

from pathlib import Path
from time import sleep
p = Path('./Proyecto/Utils/ArchivosPruebas')
action = 0

print([x for x in p.iterdir() if x.is_dir()])

# for i in range(1,10):
#     nueva_carpeta = p / str(i)
#     nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)

#     for j in range(1,10):
#         nuevo_archivo = nueva_carpeta /  ( str(j) + ".txt" )
#         nuevo_archivo.touch(0o755,True)

def mostrarMenu():
    print("\n=== MENÚ ===")
    print("1) Crear Carpetas")
    print("2) Generar Archivos")
    print("3) Eliminar Carpetas")
    print("4) Eliminar archivos")
    print("5) Salir")
    print("=" * 10)

def ejecutarAccion(accion):
    acciones = {
        1: crearDirectoriosEmergentes,
        2: crearArchivosEmergentes,
        3: eliminarDirectoriosEmergentes,
        4: eliminarArchivosEmergentes
    }

    if accion in acciones:
        acciones[accion]()
        print(f"Accion {accion} completada")
    else:
        print("Opción invalida")

def crearDirectoriosEmergentes():
    for i in range(1,10):
        nueva_carpeta = p / str(i)
        nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)

def eliminarDirectoriosEmergentes():
    for i in range(1,10):
        carpeta_usada = p / str(i)
        carpeta_usada.rmdir()

def crearArchivosEmergentes():
    for i in range(1,10):
        for j in range(1,10):
            archivo = p / str (i) / f"Tesis{j}.pdf"
            archivo.touch(755,True)

def eliminarArchivosEmergentes():
    for i in range(1,10):
        for j in range(1,10):
            archivo = p / str (i) / f"Tesis{j}.pdf"
            archivo.unlink(missing_ok=True)

            archivo = p / str (i) / f"{j}.txt"
            archivo.unlink(missing_ok=True)

            archivo = p / str (i) / f"{j}"
            archivo.unlink(missing_ok=True)
    # Eliminar archivos por nombre
    # Carpetas por nombres 


if __name__ == "__main__":
    print("Ejecute una accion:")
    print("1) Crear Carpetas")
    print("2) Generar Archivos")
    print("3) Eliminar Carpetas")
    print("4) Eliminar archivos")
    while (action < 1 or action > 4):
        print("Seleccione una opcion de la 1 a la 4:")
        action = int(input())
    print(f"Usted selecciono: {action}")
