from pathlib import Path

# Rutas
RUTA_BASE = Path('./Proyecto/Utils/ArchivosPruebas')
PERMISOS_DIR = 0o755
PERMISOS_FILE = 0o755

RANGO_CARPETAS = range(2000,2027)
RANGO_ARCHIVOS = range(1,150)

# Cron 
SCHEDULE = "0 2 * * *"
    #Cambiar este, a modo online
SYNC_COMMAND = "rsync -azv --delete ./Proyecto/Utils/ArchivosPruebas/TESIS/ ./Proyecto/Utils/ArchivosPruebas/BACKUP/"