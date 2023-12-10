import subprocess
import time
import os

scripts_folder = "python"

script_order = [
    "personas.py",
    "plazas_disponibles.py",
    "criba_bbdd.py",
    "valoraciones.py",
    "asignacion_plazas.py"
]

for script in script_order:
    script_path = os.path.join(scripts_folder, script)
    os.path.exists(script_path)
    subprocess.run(["python3", script_path])
    time.sleep(2)  


