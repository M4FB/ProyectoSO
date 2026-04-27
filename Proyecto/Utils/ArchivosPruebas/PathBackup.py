from pathlib import Path

p = Path('./Proyecto/Utils/ArchivosPruebas')

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

def contarArchivosArbol():
    contador = 0
    # Con esto contar los archivos, incluidos archivos nuevos, probablemente de esta carpeta se usa la iteracion base
    ruta_tesis = p / "TESIS" / "2009"
    for child in ruta_tesis.iterdir():
        contador += 1
    print(contador)
# Extraer los datos de carpeta antes que de archivos

crearArbolInicial()
crearArchivosBase()
contarArchivosArbol()