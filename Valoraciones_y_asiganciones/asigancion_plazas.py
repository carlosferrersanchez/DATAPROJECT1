import pymysql
from collections import defaultdict

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
    "Granda": 20,
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
    "Girona": 20,
    "Álava": 20,
    "La Rioja": 20,
    "Vizcaya": 20,
    "A Coruña": 20
}

def asignar_viajes(personas, plazas_por_provincia):
    provincias_asignadas = defaultdict(list)

    for persona in personas:
        pref1 = persona["preferencia_1"]
        pref2 = persona["preferencia_2"]
        puntuacion = persona["valoraciones_personas"]
        persona_id = persona["id_persona"]
        
        preferencias = [pref1, pref2]

    for preferencia in preferencias:
            for provincia in preferencia:
                if plazas_por_provincia[provincia] > 0:
                    plazas_por_provincia[provincia] -= 1
                    provincias_asignadas[persona_id].append(provincia)
                    break 
            else:
                continue
            break  
    

    return provincias_asignadas

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

        cursor.execute("SHOW COLUMNS FROM personas LIKE 'asignacion_experiencia'")
        resultado = cursor.fetchone()
        if not resultado:
            cursor.execute("ALTER TABLE personas ADD COLUMN asignacion_experiencia VARCHAR(50)")


        cursor.execute("SHOW COLUMNS FROM personas LIKE 'asignacion_provincia'")
        resultado = cursor.fetchone()
        if not resultado:
            cursor.execute("ALTER TABLE personas ADD COLUMN asignacion_provincia VARCHAR(50)")

        conexion.commit()
       

        consulta_personas = "SELECT id, valoraciones_personas, preferencia_1, preferencia_2 FROM personas"
        cursor.execute(consulta_personas)
        personas = cursor.fetchall()

        # Llamamos a la función para asignar los viajes
        provincias_asignadas = asignar_viajes(personas, plazas_por_provincia)

        # Actualizar la base de datos con las asignaciones de provincias a las personas
        for persona_id, provincias in provincias_asignadas.items():
            provincias_str = ",".join(provincias)
            actualizacion = f"UPDATE personas SET provincias_asignadas = '{provincias_str}' WHERE id = {persona_id}"
            cursor.execute(actualizacion)

        conexion.commit()

        print("Viajes asignados Correctamente")

        cursor.close()

except Exception as e:
    print(f"Error: {e}")
    conexion.rollback()

finally:
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("Conexión cerrada")
