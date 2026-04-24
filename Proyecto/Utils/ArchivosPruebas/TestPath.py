# Crea Carpetas, y las elimina luego de 5 segundos

from pathlib import Path
from time import sleep
p = Path('./Proyecto/Utils/ArchivosPruebas')

print([x for x in p.iterdir() if x.is_dir()])

for i in range(1,10):
    nueva_carpeta = p / str(i)
    nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)

    for j in range(1,10):
        nuevo_archivo = nueva_carpeta /  ( str(j) + ".txt" )
        nuevo_archivo.touch(0o755,True)



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
        archivo = p / str (i) / f"Tesis{i}.pdf"
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

if __name__ == "__main__":
    eliminarArchivosEmergentes()

    