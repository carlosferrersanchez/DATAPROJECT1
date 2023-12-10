import pymysql
import random

def asignacion():
    hostname = 'mysql_server'
    database = 'imserso_database'
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
            
            cursor = conexion.cursor()

            cursor.execute("SHOW COLUMNS FROM personas LIKE 'viaje_asignado'")
            resultado = cursor.fetchone()
            if not resultado:
                cursor.execute("ALTER TABLE personas ADD COLUMN viaje_asignado ENUM('Si', 'No')")

            conexion.commit()

            cursor.execute("""
                SELECT id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, preferencia_1, preferencia_2, fecha_1, fecha_2, fecha_3, Valoracion
                FROM personas
                ORDER BY Valoracion DESC, Renta ASC
            """)
            personas = cursor.fetchall()

            for persona in personas:
                id_persona, nombre, primer_apellido, segundo_apellido, dni, preferencia1, preferencia2, fecha1, fecha2, fecha3, Valoracion = persona

                preferencias = [preferencia1, preferencia2]
                fechas = [fecha1, fecha2, fecha3]

                provincia_elegida = None
                fecha_elegida = None
                fecha_viaje = None

                for preferencia in preferencias:
                    for fecha in fechas:
                        if preferencia is not None and fecha is not None:
                            cursor.execute("""
                                SELECT Ciudad, Mes, Fecha_viaje, Num_plazas
                                FROM plazas_disponibles
                                WHERE Ciudad = %s AND Mes = %s AND Num_plazas > 0
                                ORDER BY RAND() LIMIT 1
                            """, (preferencia, fecha))
                            resultado = cursor.fetchone()
                            if resultado:
                                provincia_elegida, fecha_elegida, fecha_viaje, num_plazas_disponibles = resultado
                                break

                if provincia_elegida is None:
                    for preferencia in preferencias:
                        if preferencia is not None:
                            cursor.execute("""
                                SELECT Ciudad, Mes, Fecha_viaje, Num_plazas
                                FROM plazas_disponibles
                                WHERE Ciudad = %s AND Num_plazas > 0
                                ORDER BY RAND() LIMIT 1
                            """, (preferencia,))
                            resultado = cursor.fetchone()
                            if resultado:
                                provincia_elegida, fecha_elegida, fecha_viaje, num_plazas_disponibles = resultado
                                break

                if provincia_elegida is None:
                    cursor.execute("""
                        SELECT Ciudad, Mes, Fecha_viaje, Num_plazas
                        FROM plazas_disponibles
                        WHERE Num_plazas > 0
                        ORDER BY RAND() LIMIT 1
                    """)
                    resultado = cursor.fetchone()
                    if resultado:
                        provincia_elegida, fecha_elegida, fecha_viaje, num_plazas_disponibles = resultado

                if provincia_elegida is not None and fecha_elegida is not None:
                    cursor.execute("""
                        INSERT INTO viajes_asignados 
                        (id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, Ciudad, Mes, Fecha_viaje, Valoracion) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (id_persona, nombre, primer_apellido, segundo_apellido, dni, provincia_elegida, fecha_elegida, fecha_viaje, Valoracion))
                    conexion.commit()
                    cursor.execute("""
                        UPDATE plazas_disponibles
                        SET Num_plazas = Num_plazas - 1
                        WHERE Ciudad = %s AND Mes = %s
                    """, (provincia_elegida, fecha_elegida))
                    conexion.commit()

                    cursor.execute("""
                        UPDATE personas
                        SET viaje_asignado = 'Si'
                        WHERE id_persona = %s
                    """, (id_persona,))
                    conexion.commit()

                else:
                    cursor.execute("""
                        INSERT INTO lista_espera (id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, Valoracion)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (id_persona, nombre, primer_apellido, segundo_apellido, dni, Valoracion))
                    conexion.commit()

                    cursor.execute("""
                        UPDATE personas
                        SET viaje_asignado = 'No'
                        WHERE id_persona = %s
                    """, (id_persona,))
                    conexion.commit()

            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        if 'conexion' in locals() and conexion.open:
            conexion.close()
            print(f'Viajes asignados correctamente. \n'
                f'Conexión cerrada')
