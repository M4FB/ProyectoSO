from pathlib import Path
# Aleatorizar Tamaños
import random
import os
# Rsync para Verificar
import subprocess


p = Path('./Proyecto/Utils/ArchivosPruebas')

def crearBackup():
    subprocess.run(['rsync', '-az', '--delete', './Proyecto/Utils/ArchivosPruebas/TESIS/', 
                './Proyecto/Utils/ArchivosPruebas/BACKUP/'])

def crearArbolInicial():
    # Arbol Tesis / 2020-2026
    carpeta_base = p / "TESIS"
    carpeta_base.mkdir(0o777,parents=False,exist_ok=True)
    for i in range(2000,2027):
        nueva_carpeta = carpeta_base / str(i)
        nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)

def crearArchivosBase():
    # for i in range(2000,2027):
    #     for j in range(1,150):
    #         archivoParaCrear = p / "TESIS" / str(i) / f"Tesis_{i}_{j}.pdf"
    #         archivoParaCrear.touch()

    for i in range(2000,2027):
        for j in range(1,150):
            archivoParaCrear = p / "TESIS" / str(i) / f"Tesis_{i}_{j}.pdf"

            tamanio_kb = random.randint(89, 190)
            tamanio_bytes = tamanio_kb * 1024
            
            archivoParaCrear.write_bytes(os.urandom(tamanio_bytes))

# comparar carpetas 

def compararCarpetas():
    carpetaBk = p / "BACKUP"
    nuevopath = p / "TESIS"
    for carpetaChild in nuevopath.iterdir():
        print(carpetaChild)
# comparar numeros

def contarArchivosArbol():
    contador = 0
    # Con esto contar los archivos, incluidos archivos nuevos, probablemente de esta carpeta se usa la iteracion base
    ruta_tesis = p / "TESIS" / "2009"
    for child in ruta_tesis.iterdir():
        contador += 1
    print(contador)
# Extraer los datos de carpeta antes que de archivos
# No es necesario contar archivo por archivo, con ver si una carpeta cambia basta

# crearArbolInicial()
# crearArchivosBase()
# contarArchivosArbol()
# compararCarpetas()
crearArbolInicial()
crearArchivosBase()
crearBackup()


# path_bk = p / "BACKUP" / "2020"
# path_or = p / "TESIS" / "2020"
# # rsync
# for childFolder in path_or.iterdir():
#     # print(childFolder.stat())
#     backupFolder = path_bk / childFolder.name
    
#     archivoParaModificar = path_bk / "Tesis_2020_130.pdf"
#     archivoParaModificar.write_bytes(os.urandom(20000))


#     folderSizeComp = childFolder.stat().st_size != backupFolder.stat().st_size
    
 
#     # Comparar tamaño 2 archivos:
#     print(childFolder.stat().st_size)
#     print(backupFolder.stat().st_size)
#     print(f"La carpeta: {childFolder.name} Cambio?:{folderSizeComp}")
