#!/bin/bash

# Otorgar permisos de ejecución al script Python cada vez que se ejecute este script
chmod +x mysql_server/conexion_test.py

# Ir al directorio donde se encuentra el docker-compose.yml y el script Python
cd mysql_server

# Iniciar los contenedores definidos en el docker-compose.yml
docker-compose up -d

# Esperar un momento para asegurarse de que el contenedor esté en funcionamiento
sleep 5

# Ejecutar tu script de Python que establece la conexión automáticamente
python3 conexion_test.py


