import pymysql

hostname = '127.0.0.1'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

## Funciones para hacer Valoraciones y sumar puntos ##

def actualizar_valoracion(cursor, id_persona, valoracion):
    consulta = "UPDATE personas SET valoraciones_personas = %s WHERE id = %s"
    cursor.execute(consulta, (valoracion, id_persona))
    
def valoracion_renta_economica(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN renta < 6700 THEN (valoraciones_personas + 70)
                WHEN renta BETWEEN 6700 AND 13000 THEN (valoraciones_personas + 60)
                WHEN renta BETWEEN 13001 AND 20000 THEN (valoraciones_personas + 50)
                WHEN renta BETWEEN 20001 AND 35000 THEN (valoraciones_personas + 40)
                WHEN renta BETWEEN 35001 AND 60000 THEN (valoraciones_personas + 30)
                WHEN renta BETWEEN 60001 AND 100000 THEN (valoraciones_personas + 20)
                WHEN renta BETWEEN 100001 AND 300000 THEN (valoraciones_personas + 10)
                WHEN renta > 300001 THEN (valoraciones_personas + 0)
            END
        """
    cursor.execute(consulta)

def valoracion_participaciones_anteriores(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN numero_participaciones = 0 THEN (valoraciones_personas + 30)
                WHEN numero_participaciones BETWEEN 1 AND 2 THEN (valoraciones_personas + 18)
                WHEN numero_participaciones BETWEEN 3 AND 6 THEN (valoraciones_personas + 12)
                WHEN numero_participaciones BETWEEN 7 AND 10 THEN (valoraciones_personas + 6)
                WHEN numero_participaciones > 10 THEN (valoraciones_personas + 0)
            END
        """
    cursor.execute(consulta)

def valoracion_aislamiento_social(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN vive_solo = 0 THEN (valoraciones_personas + 0)
                WHEN vive_solo = 1 THEN (valoraciones_personas + 30)
            END
        """
    cursor.execute(consulta)

def valoracion_grado_discapacidad(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN grado_discapacidad = 0 THEN (valoraciones_personas + 0)
                WHEN grado_discapacidad = 1 THEN (valoraciones_personas + 20)
                WHEN grado_discapacidad = 2 THEN (valoraciones_personas + 30)
                END
            """
    cursor.execute(consulta)

def valoracion_disc_multiple(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN tipo_discapacidad = 'Multiple' THEN (valoraciones_personas + 10)
                END
            """
    cursor.execute(consulta)

def valoracion_edad(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN edad BETWEEN 55 AND 59 THEN (valoraciones_personas + 0)
                WHEN edad BETWEEN 60 AND 64 THEN (valoraciones_personas + 5)
                WHEN edad BETWEEN 65 AND 69 THEN (valoraciones_personas + 15)
                WHEN edad BETWEEN 70 AND 74 THEN (valoraciones_personas + 20)
                WHEN edad BETWEEN 75 AND 79 THEN (valoraciones_personas + 25)
                WHEN edad > 80 THEN (valoraciones_personas + 30)
                ELSE 0
                END
            """
    cursor.execute(consulta)

def valoracion_personas_dependientes(cursor):
    consulta = """
        UPDATE personas
        SET valoraciones_personas =
            CASE
                WHEN personas_dependientes = 0 THEN (valoraciones_personas + 0)
                WHEN personas_dependientes = 1 THEN (valoraciones_personas + 4)
                WHEN personas_dependientes = 2 THEN (valoraciones_personas + 6)
                WHEN personas_dependientes = 3 THEN (valoraciones_personas + 8)
                WHEN personas_dependientes > 4 THEN (valoraciones_personas + 10)
                END
            """
    cursor.execute(consulta)    


## Conexion a la BBDD para las valoraciones ##

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

        ## Comprobar si la columna "valoraciones_personas" existe, para borrarla en caso de que si ##

        cursor.execute("SHOW COLUMNS FROM personas LIKE 'valoraciones_personas'")
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("ALTER TABLE personas DROP COLUMN valoraciones_personas")

        ## Creación de la columna "valoraciones_columnas" con valor inicial 0 ##

        nueva_columna = "ALTER TABLE personas ADD valoraciones_personas int DEFAULT 0"
        cursor.execute(nueva_columna)

        ## Llamada a funciones para hacer Valoraciones ##

        valoracion_renta_economica(cursor)
        valoracion_participaciones_anteriores(cursor)
        valoracion_aislamiento_social(cursor)
        valoracion_grado_discapacidad(cursor)
        valoracion_disc_multiple(cursor)
        valoracion_edad(cursor)
        valoracion_personas_dependientes(cursor)

        conexion.commit()

        print("Valoración de las Personas Solicitantes ejecutada")

        cursor.close()

except Exception as e:
    print(f"Error: {e}")
    conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("-------------------------------------------------------------\n"
              "Conexión cerrada\n"
              "-------------------------------------------------------------")
