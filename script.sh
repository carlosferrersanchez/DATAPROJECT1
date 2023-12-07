#!/bin/bash

chmod +x mysql_server/conexion.py

cd mysql_server

pip3 install -r requirements.txt

docker-compose up -d

sleep 5

python3 conexion.py


