from pathlib import Path
import subprocess
import os
import random
from config import *
p = RUTA_BASE

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
        1: crearDirectoriosIniciales,
        2: crearArchivosBase,
        3: crearCronBackup,
        4: forzarBackup
    }

    if accion in acciones:
        acciones[accion]()
        print(f"Accion {accion} completada")
    else:
        print("Opción invalida")

def crearBackup():
    subprocess.run(['rsync', '-az', '--delete', './Proyecto/Utils/ArchivosPruebas/TESIS/', 
                './Proyecto/Utils/ArchivosPruebas/BACKUP/'])

def crearCronBackup():
    pass

def forzarBackup():
    pass

def crearDirectoriosIniciales():
    carpeta_base = p / "TESIS"
    carpeta_base.mkdir(PERMISOS_DIR,parents=False,exist_ok=True)
    for i in range(2000,2027):
        nueva_carpeta = carpeta_base / str(i)
        nueva_carpeta.mkdir(mode=PERMISOS_DIR, parents=False,exist_ok=True)

def crearArchivosBase():
    for i in RANGO_CARPETAS:
        for j in RANGO_ARCHIVOS:
            archivoParaCrear = p / "TESIS" / str(i) / NOMBRE_PDF
            tamanio_kb = random.randint(89, 190)
            tamanio_bytes = tamanio_kb * 1024    
            archivoParaCrear.write_bytes(os.urandom(tamanio_bytes))

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
