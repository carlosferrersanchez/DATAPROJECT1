import pymysql

def valoraciones():

    hostname = 'mysql_server'
    database = 'imserso_database'
    username = 'user'
    password = 'admin01'
        
    def valoracion_renta_economica(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                        WHEN renta < 6700 THEN 66
                        WHEN renta BETWEEN 6700 AND 13000 THEN 55
                        WHEN renta BETWEEN 13001 AND 20000 THEN 44
                        WHEN renta BETWEEN 20001 AND 35000 THEN 33
                        WHEN renta BETWEEN 35001 AND 60000 THEN 22
                        WHEN renta BETWEEN 60001 AND 100000 THEN 11
                        WHEN renta > 100001 THEN 0
                    END
            """
        cursor.execute(consulta)

    def valoracion_participaciones_anteriores(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN numero_participaciones = 0 THEN (Valoracion + 30)
                    WHEN numero_participaciones BETWEEN 1 AND 2 THEN (Valoracion + 18)
                    WHEN numero_participaciones BETWEEN 3 AND 6 THEN (Valoracion + 12)
                    WHEN numero_participaciones BETWEEN 7 AND 10 THEN (Valoracion + 6)
                    WHEN numero_participaciones > 10 THEN (Valoracion + 0)
                END
            """
        cursor.execute(consulta)

    def valoracion_aislamiento_social(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN vive_solo = 0 THEN (Valoracion + 0)
                    WHEN vive_solo = 1 THEN (Valoracion + 25)
                END
            """
        cursor.execute(consulta)

    def valoracion_grado_discapacidad(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN grado_discapacidad = 0 THEN (Valoracion + 0)
                    WHEN grado_discapacidad = 1 THEN (Valoracion + 20)
                    WHEN grado_discapacidad = 2 THEN (Valoracion + 30)
                    ELSE Valoracion + 0
                    END
                """
        cursor.execute(consulta)

    def valoracion_disc_multiple(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN tipo_discapacidad = 'Multiple' THEN (Valoracion + 10)
                    ELSE Valoracion + 0
                    END
                """
        cursor.execute(consulta)

    def valoracion_edad(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN edad BETWEEN 55 AND 59 THEN (Valoracion + 0)
                    WHEN edad BETWEEN 60 AND 64 THEN (Valoracion + 7)
                    WHEN edad BETWEEN 65 AND 69 THEN (Valoracion + 14)
                    WHEN edad BETWEEN 70 AND 74 THEN (Valoracion + 21)
                    WHEN edad BETWEEN 75 AND 79 THEN (Valoracion + 28)
                    WHEN edad > 80 THEN (Valoracion + 35)
                    ELSE Valoracion + 0
                    END
                """
        cursor.execute(consulta)

    def valoracion_personas_dependientes(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN personas_dependientes = 0 THEN (Valoracion + 0)
                    WHEN personas_dependientes = 1 THEN (Valoracion + 4)
                    WHEN personas_dependientes = 2 THEN (Valoracion + 6)
                    WHEN personas_dependientes = 3 THEN (Valoracion + 8)
                    WHEN personas_dependientes > 4 THEN (Valoracion + 10)
                    END
                """
        cursor.execute(consulta)    

    def valoracion_obras_sociales(cursor):
        consulta = """
            UPDATE personas
            SET Valoracion =
                CASE
                    WHEN obras_sociales = 'No' THEN (Valoracion + 0)
                    WHEN obras_sociales = '1-6 dias' THEN (Valoracion + 3)
                    WHEN obras_sociales = '7-30 dias' THEN (Valoracion + 6)
                    WHEN obras_sociales = '1-3 meses' THEN (Valoracion + 9)
                    WHEN obras_sociales = '+3 meses' THEN (Valoracion + 10)
                    END
                """
        cursor.execute(consulta)    

    try:
        conexion = pymysql.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        if conexion.open:

            cursor = conexion.cursor()

            cursor.execute("SHOW COLUMNS FROM personas LIKE 'Valoracion'")
            resultado = cursor.fetchone()

            if not resultado:
                cursor.execute("ALTER TABLE personas ADD COLUMN Valoracion int DEFAULT 0")

            conexion.commit()

            valoracion_renta_economica(cursor)
            valoracion_participaciones_anteriores(cursor)
            valoracion_aislamiento_social(cursor)
            valoracion_grado_discapacidad(cursor)
            valoracion_disc_multiple(cursor)
            valoracion_edad(cursor)
            valoracion_personas_dependientes(cursor)
            valoracion_obras_sociales(cursor)


            conexion.commit()
            print("Valoración de las Personas Solicitantes ejecutada")

            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        if 'conexion' in locals() and conexion.open:
            conexion.close()
