import pymysql
import random

hostname = '127.0.0.1'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

viaje_montaña_provincias = {
    "Asturias": 20,
    "Cantabria": 20,
    "Huesca": 20,
    "Lérida": 20,
    "Navarra": 20,
    "Granada": 20,
    "Lugo": 20
}

viaje_cultural_provincias = {
    "Burgos": 20,
    "Cuenca": 20,
    "Segovia": 20,
    "Zaragoza": 20,
    "Cáceres": 20,
    "León": 20,
    "Sevilla": 20,
    "Toledo": 20,
    "Ávila": 20,
    "Córdoba": 20,
    "Salamanca": 20,
    "Valladolid": 20
}

viaje_rural_provincias = {
    "Pontevedra": 20,
    "Zamora": 20,
    "Albacete": 20,
    "Badajoz": 20,
    "Ciudad Real": 20,
    "Guadalajara": 20,
    "Jaén": 20,
    "Orense": 20,
    "Palencia": 20,
    "Soria": 20,
    "Teruel": 20
}

viaje_islas_provincias = {
    "Santa Cruz de Tenerife": 20,
    "Las Palmas": 20,
    "Islas Baleares": 20
}

viaje_playa_provincias = {
    "Alicante": 20,
    "Almeria": 20,
    "Cadiz": 20,
    "Castellón": 20,
    "Girona": 20,
    "Huelva": 20,
    "Málaga": 20,
    "Murcia": 20,
    "Tarragona": 20
}

viaje_gastronómico_provincias = {
    "Barcelona": 20,
    "Guipúzcoa": 20,
    "Madrid": 20,
    "Valencia": 20,
    "Álava": 20,
    "La Rioja": 20,
    "Vizcaya": 20,
    "A Coruña": 20
}


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

        cursor.execute("""
            SELECT id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, preferencia_1, preferencia_2, fecha_1, fecha_2, fecha_3
            FROM personas
        """)
        personas = cursor.fetchall()

        for persona in personas:
            id_persona = persona[0]
            nombre = persona[1]
            primer_apellido = persona[2]
            segundo_apellido = persona[3]
            dni = persona[4]
            preferencia1 = persona[5]
            preferencia2 = persona[6]
            fecha1 = persona[7]
            fecha2 = persona[8]
            fecha3 = persona[9]

            viajes_disponibles = {
                "Montaña": viaje_montaña_provincias,
                "Cultural": viaje_cultural_provincias,
                "Playa": viaje_playa_provincias,
                "Gastronómico": viaje_gastronómico_provincias,
                "Islas": viaje_islas_provincias,
                "Rural": viaje_rural_provincias,
            }

            for fecha in [fecha1, fecha2, fecha3]:
                for preferencia in [preferencia1, preferencia2]:
                    if preferencia in viajes_disponibles:
                        provincias_disponibles = viajes_disponibles[preferencia]
                        if len(provincias_disponibles) > 0:
                            provincia_elegida = random.choice(list(provincias_disponibles.keys()))
                            plazas_disponibles = provincias_disponibles[provincia_elegida]

                            if plazas_disponibles > 0:
                                cursor.execute("""
                                    INSERT INTO viajes_asignados 
                                    (id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, Ciudad, Mes, Valoracion) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                """, (id_persona, nombre, primer_apellido, segundo_apellido, dni, provincia_elegida, fecha, 0))
                                conexion.commit()
                                print(f"Viaje asignado a la persona {id_persona}: {preferencia} - {provincia_elegida}")
                                provincias_disponibles[provincia_elegida] -= 1
                                break
                            else:
                                del provincias_disponibles[provincia_elegida]
                        else:
                            print(f"No hay provincias disponibles para {preferencia} para la persona {id_persona}")
                    else:
                        print(f"Preferencia '{preferencia}' no encontrada para la persona {id_persona}")

                else:
                    continue  # Este bloque se ejecuta si el bucle interno se completa sin un "break"

                break  # Este bloque se ejecuta si el bucle interno se rompe con un "break"

            else:
                cursor.execute("""
                    INSERT INTO lista_espera (id_persona, Nombre, Primer_apellido, Segundo_apellido, DNI, Valoracion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (id_persona, nombre, primer_apellido, segundo_apellido, dni, 0))
                conexion.commit()
                print(f"No hay viajes disponibles para la persona {id_persona}, se agregó a la lista de espera")

        cursor.close()

except Exception as e:
    print(f"Error: {e}")
    conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("Conexión cerrada")