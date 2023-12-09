import pandas as pd
import pymysql
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('es_ES')

# Generar datos aleatorios para plazas_disponibles
datos_plazas = []

for i in range(600):
    ciudad = fake.city()
    hotel = f'Hotel_{random.randint(1, 10)}' # CAMBIAR ESTO
    estrellas_hotel = random.randint(3, 5)
    zona_destino = f'Zona_{random.randint(1, 5)}' # CAMBIAR ESTO
    tipo_exp = f'Tipo_{random.randint(1, 3)}' # CAMBIAR ESTO
    mes = random.choice(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
    fecha_viaje = (datetime.now() + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
    num_plazas = 9

    datos_plazas.append((ciudad, hotel, estrellas_hotel, zona_destino, tipo_exp, mes, fecha_viaje, num_plazas))

# Insertar datos en la tabla 'plazas_disponibles'
hostname = '127.0.0.1'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

try:
    conexion = pymysql.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    if conexion.open:
        print("-------------------------------------------------------------\n"
             "Conexión establecida\n"
             "-------------------------------------------------------------")

        nombre_tabla_plazas = 'plazas_disponibles'

        columnas_plazas = ['Ciudad', 'Hotel', 'Estrellas_hotel', 'Zona_destino', 'Tipo_exp', 'Mes', 'Fecha_viaje', 'Num_plazas']
        marcadores_plazas = ', '.join(['%s'] * len(columnas_plazas))
        consulta_plazas = f"INSERT INTO {nombre_tabla_plazas} ({', '.join(columnas_plazas)}) VALUES ({marcadores_plazas})"

        cursor_plazas = conexion.cursor()
        cursor_plazas.executemany(consulta_plazas, datos_plazas)
        conexion.commit()

        print(f"600 destinos insertados correctamente en la tabla '{nombre_tabla_plazas}' de la base de datos '{database}'")

except Exception as e:
    print(f"Error desconocido: {e}")
finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("-------------------------------------------------------------\n"
              "Conexión cerrada")