from pathlib import Path
import shutil

p = Path('./Proyecto/Utils/ArchivosPruebas')

def crearBackup():
    path_bk = p / "BACKUP"
    path_or = p / "TESIS"
    path_bk.mkdir(exist_ok=True)

    for childFolder in path_or.iterdir():
        destino = path_bk / childFolder.name
        childFolder.copy(destino, preserve_metadata=True)

def crearArbolInicial():
    # Arbol Tesis / 2020-2026
    carpeta_base = p / "TESIS"
    carpeta_base.mkdir(0o777,parents=False,exist_ok=True)
    for i in range(2000,2027):
        nueva_carpeta = carpeta_base / str(i)
        nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)

def crearArchivosBase():
    for i in range(2000,2027):
        for j in range(1,150):
            archivoParaCrear = p / "TESIS" / str(i) / f"Tesis_{i}_{j}.pdf"
            archivoParaCrear.touch()

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

crearArbolInicial()
crearArchivosBase()
contarArchivosArbol()
compararCarpetas()
crearBackup()