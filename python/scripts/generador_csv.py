import os
import pymysql
import pandas as pd

def exportar_a_csv(tabla, nombre_archivo, ruta='/data'):
    try:
        # Utilizar los mismos detalles de conexión que en tus otros scripts
        conexion = pymysql.connect(
            host='mysql_server',
            user='user',
            password='admin01',
            database='imserso_database'
        )

        if conexion.open:
            # Leer datos de la tabla con pandas
            consulta = f"SELECT * FROM {tabla}"
            df = pd.read_sql_query(consulta, conexion)

            # Construir la ruta completa del archivo CSV
            ruta_completa = os.path.join(ruta, f"{nombre_archivo}")

            # Exportar a archivo CSV
            df.to_csv(ruta_completa, index=False)
            print(f"Datos de la tabla {tabla} exportados a {ruta_completa}")

    except Exception as e:
        print(f"Error al exportar datos de la tabla {tabla}: {e}")

    finally:
        if 'conexion' in locals() and conexion.open:
            conexion.close()
