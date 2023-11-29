import pandas as pd
import pymysql
from creacion_database import personas_imserso

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
        print("Conexión establecida")

        nombre_tabla = 'personas'

        valores = personas_imserso.values.tolist()

        columnas = ', '.join(personas_imserso.columns)
        marcadores = ', '.join(['%s'] * len(personas_imserso.columns))
        consulta = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({marcadores})"

        cursor = conexion.cursor()
        cursor.executemany(consulta, valores)
        conexion.commit()

        print(f"Datos insertados correctamente en la tabla '{nombre_tabla}' de la base de datos '{database}'")

except pymysql.err.OperationalError as e:
    print(f"Error de conexión: {e}")
except pymysql.err.ProgrammingError as e:
    print(f"Error en la consulta SQL: {e}")
except Exception as e:
    print(f"Error desconocido: {e}")
finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("Conexión cerrada")


