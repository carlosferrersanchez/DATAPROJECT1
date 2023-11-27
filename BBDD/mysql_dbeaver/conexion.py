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
        database=database
    )

    if conexion.is_connected():
        print("Conexión establecida")
        
except mysql.connector.Error as e:
    print(f"No se ha podido establecer conexión: {e}")
finally:
    # Cierra la conexión fuera del bloque try-except para asegurar que se cierre incluso si hay una excepción.
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")