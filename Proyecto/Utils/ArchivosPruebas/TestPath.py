from pathlib import Path
from time import sleep
p = Path('./Proyecto/Utils/ArchivosPruebas')

print([x for x in p.iterdir() if x.is_dir()])

for i in range(1,10):
    nueva_carpeta = p / str(i)
    nueva_carpeta.mkdir(mode=0o777, parents=False,exist_ok=True)


sleep(5)

for i in range(1,10):
    vieja_carpeta = p / str(i)
    vieja_carpeta.rmdir()