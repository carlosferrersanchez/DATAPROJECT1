:: script.bat

icacls mysql_server\conexion.py /grant Everyone:F

cd mysql_server

pip install -r requirements.txt

docker-compose up -d

timeout /t 5 /nobreak

python conexion.py