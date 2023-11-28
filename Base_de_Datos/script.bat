:: script.bat

:: Dar permisos de ejecución al archivo conexion_test.py (equivalente a chmod +x en Bash)
icacls mysql_server\conexion_test.py /grant Everyone:F

:: Cambiar al directorio mysql_server
cd mysql_server

:: Instalar los requisitos del proyecto
pip install -r requirements.txt

:: Iniciar los servicios con Docker Compose
docker-compose up -d

:: Esperar 5 segundos
timeout /t 5 /nobreak

:: Ejecutar el script de Python
python conexion_test.py