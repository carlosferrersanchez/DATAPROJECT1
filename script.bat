:: script.bat

icacls conexion.py /grant Everyone:F

pip install -r requirements.txt

docker-compose up -d

timeout /t 5 /nobreak

python conexion.py