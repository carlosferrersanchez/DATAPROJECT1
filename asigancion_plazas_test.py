import pymysql
import random

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
        cursor = conexion.cursor()

        cursor.execute("SHOW COLUMNS FROM personas LIKE 'asignacion_viaje'")
        asignacion_viaje_column = cursor.fetchone()
        if asignacion_viaje_column is None:
            cursor.execute("ALTER TABLE personas ADD COLUMN asignacion_viaje VARCHAR(50)")

        cursor.execute("SHOW COLUMNS FROM personas LIKE 'asignacion_provincia'")
        asignacion_provincia_column = cursor.fetchone()
        if asignacion_provincia_column is None:
            cursor.execute("ALTER TABLE personas ADD COLUMN asignacion_provincia VARCHAR(50)")




except Exception as e:
    print(f"Error: {e}")
    conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("Conexión cerrada")