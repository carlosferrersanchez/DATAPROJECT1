#!/bin/bash

chmod +x conexion.py

pip3 install -r requirements.txt

docker-compose up -d

sleep 5

python3 conexion.py


