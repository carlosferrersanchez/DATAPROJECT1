import mysql.connector

hostname = 'localhost'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

try:
    conexion = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
    )

    if conexion.is_connected():
        print("Conexión establecida")

        # Crea un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Crea la base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

except mysql.connector.Error as e:
    print(f"No se ha podido establecer conexión: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        # Cierra el cursor antes de cerrar la conexión
        cursor.close()
        conexion.close()
        print("Conexión cerrada")