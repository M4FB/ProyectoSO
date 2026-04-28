from pathlib import Path
import subprocess
import os
import random
from config import *
p = RUTA_BASE

#Opciones Menu
def mostrarMenu():
    print("\n=== MENÚ ===")
    print("1) Crear Estructura Inicial (Archivos y Carpetas)")
    print("2) Forzar Backup")
    print("3) Eliminar Carpetas")
    print("4) Eliminar archivos")
    print("5) Salir")
    print("=" * 10)

def ejecutarAccion(accion):
    acciones = {
        1: crearEstructuraInicial,
        2: forzarBackup,
        3: crearCronBackup,
        4: eliminarEstructuras
    }

    if accion in acciones:
        acciones[accion]()
        print(f"Accion {accion} completada")
    else:
        print("Opción invalida")

#Acciones a Realizar

def crearCronBackup():
    pass

def eliminarEstructuras():
    pass

def forzarBackup():
     subprocess.run(['rsync', '-azv', '--delete', './Proyecto/Utils/ArchivosPruebas/TESIS/', 
                './Proyecto/Utils/ArchivosPruebas/BACKUP/'])

def crearEstructuraInicial():
    carpeta_base = p / "TESIS"
    carpeta_base.mkdir(PERMISOS_DIR,parents=False,exist_ok=True)
    
    for i in RANGO_CARPETAS:
        nueva_carpeta = carpeta_base / str(i)
        nueva_carpeta.mkdir(mode=PERMISOS_DIR, parents=False,exist_ok=True)

        for j in RANGO_ARCHIVOS:
            archivoParaCrear = p / "TESIS" / str(i) / f"Tesis{i}_{j}.pdf"
            tamanio_kb = random.randint(89, 190)
            tamanio_bytes = tamanio_kb * 1024    
            archivoParaCrear.write_bytes(os.urandom(tamanio_bytes))

# def eliminarArchivosEmergentes():
#     for i in range(1,10):
#         for j in range(1,10):
#             archivo = p / str (i) / f"Tesis{j}.pdf"
#             archivo.unlink(missing_ok=True)

#             archivo = p / str (i) / f"{j}.txt"
#             archivo.unlink(missing_ok=True)

#             archivo = p / str (i) / f"{j}"
#             archivo.unlink(missing_ok=True)
    # Eliminar archivos por nombre
    # Carpetas por nombres 


if __name__ == "__main__":
    while True:
        mostrarMenu()
        try:
            accion = int(input("Selecciona opción: "))
            if accion == 5:
                print("Finalizado")
                break
            ejecutarAccion(accion)
        except ValueError:
            print("Error, ingrese una opcion valida")
        except Exception as e:
            print(f"Error: {e}")
