import pymysql

hostname = '127.0.0.1'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

# Funciones para las características excluyentes #

def excluye_no_espanoles_fuera_espana(cursor):
    # Excluye a los NO españoles que NO residan en España
    consulta = "DELETE FROM personas WHERE nacionalidad != 'España' AND pais_residencia != 'España'"
    cursor.execute(consulta)

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

        cursor = conexion.cursor()

        # Ejecutar las funciones para excluir personas según características
        excluye_no_espanoles_fuera_espana(cursor)

        # Confirmar los cambios en la base de datos
        conexion.commit()

        print("Personas eliminadas según las características excluyentes")

        cursor.close()

except Exception as e:
    print(f"Error desconocido: {e}")
    conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("-------------------------------------------------------------\n"
              "Conexión cerrada")
