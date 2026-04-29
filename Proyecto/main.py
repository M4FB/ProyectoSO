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
def crearCronBackup(schedule = SCHEDULE, command = SYNC_COMMAND):
    resultado = subprocess.run(["crontab","-1"],capture_output=True,text=True)
    archivoActual = resultado.stdout if resultado.returncode == 0 else ""

    nuevoCronJob= f"{schedule} {command}\n"

    if nuevoCronJob in archivoActual:
        print("La tarea ya fue implementada en el sistema.")
        return
    
    nuevoCronTab = archivoActual + nuevoCronJob
    subprocess.run(["crontab","-"], input=nuevoCronTab, text=True,check=True)
    print(f"Tarea Creada: {nuevoCronJob.strip()}")




def eliminarEstructuras():
    pass

def forzarBackup():
     subprocess.run(['rsync', '-azv', '--delete', './Proyecto/Utils/ArchivosPruebas/TESIS/', 
                './Proyecto/Utils/ArchivosPruebas/BACKUP/'])

def crearEstructuraInicial():
    # Carpeta base Tesis creada
    carpeta_base = p / "TESIS"
    carpeta_base.mkdir(PERMISOS_DIR,parents=False,exist_ok=True)
    
    # Rango de carpetas por años creada
    for i in RANGO_CARPETAS:
        nueva_carpeta = carpeta_base / str(i)
        nueva_carpeta.mkdir(mode=PERMISOS_DIR, parents=False,exist_ok=True)

        for j in RANGO_ARCHIVOS:
            archivoParaCrear = nueva_carpeta / f"Tesis{i}_{j}.pdf"
            tamanio_kb = random.randint(89, 190)
            tamanio_bytes = tamanio_kb * 1024    
            archivoParaCrear.write_bytes(os.urandom(tamanio_bytes))

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
