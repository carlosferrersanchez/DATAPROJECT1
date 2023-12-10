import pandas as pd
import pymysql
from faker import Faker
import random
from datetime import datetime, timedelta

def plazas_disponibles():
    fake = Faker('es_ES')

    hoteles = [
        'Hotel_Luna_de_Plata',
        'Hotel_Maravilla_del_Sol',
        'Hotel_Azahar_Perfecto',
        'Hotel_Brillo_Estelar',
        'Hotel_Canto_del_Amanecer',
        'Hotel_Luz_de_Laurel',
        'Hotel_Mística_Noche',
        'Hotel_Cumbre_Esmeralda',
        'Hotel_Oasis_Dorado',
        'Hotel_Velero_Luminoso',
        'Hotel_La_Torre_Marina',
        'Hotel_Aurora_Radiante',
        'Hotel_Rayo_de_Luz',
        'Hotel_Alborada_Mágica',
        'Hotel_Verde_Encanto',
        'Hotel_Aura_Floral',
        'Hotel_Llano_Crístal',
        'Hotel_Mil_Noche',
        'Hotel_Sueño_Radiante',
        'Hotel_Cascada_Susurrante',
        'Hotel_Corazón_de_Fuego',
        'Hotel_Rincón_de_Arcilla',
        'Hotel_Faro_Aurora',
        'Hotel_Puesta_del_Sol',
        'Hotel_Romance_Nocturno',
        'Hotel_Paraje_Soleado',
        'Hotel_Cielo_Estrellado',
        'Hotel_Brisa_Marina',
        'Hotel_Tierra_de_Esperanza',
        'Hotel_Maravilla_Nocturna',
        'Hotel_Luz_Solar',
        'Hotel_Misterio_Azul',
        'Hotel_Brisa_de_Montaña',
        'Hotel_Amor_Eterno',
        'Hotel_Estrella_Fugaz',
        'Hotel_Aurora_Boreal',
        'Hotel_Luz_de_Orquídea',
        'Hotel_Verde_Valle',
        'Hotel_Cielo_Almendra',
        'Hotel_Calma_Nocturna',
        'Hotel_Tesoro_Verde',
        'Hotel_Esencia_Astral',
        'Hotel_Monte_Sagrado',
        'Hotel_Llave_de_Luz',
        'Hotel_Mil_Sueños',
        'Hotel_Monte_Esmeralda',
        'Hotel_Mariposa_Nocturna',
        'Hotel_Cristal_Azul',
        'Hotel_Luz_de_Sueños',
        'Hotel_Vista_Estelar'
    ]

    ciudades = [
        "Asturias",
        "Cantabria",
        "Huesca",
        "Lérida",
        "Navarra",
        "Granada",
        "Lugo",
        "Burgos",
        "Cuenca",
        "Segovia",
        "Zaragoza",
        "Cáceres",
        "León",
        "Sevilla",
        "Toledo",
        "Ávila",
        "Córdoba",
        "Salamanca",
        "Valladolid",
        "Pontevedra",
        "Zamora",
        "Albacete",
        "Badajoz",
        "Ciudad Real",
        "Guadalajara",
        "Jaén",
        "Orense",
        "Palencia",
        "Soria",
        "Teruel",
        "Santa Cruz de Tenerife",
        "Las Palmas",
        "Islas Baleares",
        "Alicante",
        "Almeria",
        "Cadiz",
        "Castellón",
        "Girona",
        "Huelva",
        "Málaga",
        "Murcia",
        "Tarragona",
        "Barcelona",
        "Guipúzcoa",
        "Madrid",
        "Valencia",
        "Álava",
        "La Rioja",
        "Vizcaya",
        "A Coruña"
    ]

    viaje_montaña_provincias = [
        "Asturias",
        "Cantabria",
        "Huesca",
        "Lérida",
        "Navarra",
        "Granada",
        "Lugo"
    ]

    viaje_cultural_provincias = [
        "Burgos",
        "Cuenca",
        "Segovia",
        "Zaragoza",
        "Cáceres",
        "León",
        "Sevilla",
        "Toledo",
        "Ávila",
        "Córdoba",
        "Salamanca",
        "Valladolid"
    ]

    viaje_rural_provincias = [
        "Pontevedra",
        "Zamora",
        "Albacete",
        "Badajoz",
        "Ciudad Real",
        "Guadalajara",
        "Jaén",
        "Orense",
        "Palencia",
        "Soria",
        "Teruel"
    ]

    viaje_islas_provincias = [
        "Santa Cruz de Tenerife",
        "Las Palmas",
        "Islas Baleares"
    ]

    viaje_playa_provincias = [
        "Alicante",
        "Almeria",
        "Cadiz",
        "Castellón",
        "Girona",
        "Huelva",
        "Málaga",
        "Murcia",
        "Tarragona"
    ]

    viaje_gastronómico_provincias = [
        "Barcelona",
        "Guipúzcoa",
        "Madrid",
        "Valencia",
        "Álava",
        "La Rioja",
        "Vizcaya",
        "A Coruña"
    ]


    datos_plazas = []
    meses_del_año = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    estrellas_por_hotel = {hotel: random.randint(3, 5) for hotel in hoteles}

    for ciudad in ciudades:
        hotel = hoteles.pop(random.randint(0, len(hoteles) - 1))  
        
        meses_procesados = set()

        for mes in meses_del_año:  
            if mes in meses_procesados:
                continue

            meses_procesados.add(mes)

            primer_dia_mes = datetime(2024, meses_del_año.index(mes) + 1, 1)
            dia = random.randint(1, 22) 
            fecha_viaje_inicio = primer_dia_mes + timedelta(days=dia - 1)
            fecha_viaje_fin = fecha_viaje_inicio + timedelta(days=6)
            fecha_viaje = f'{fecha_viaje_inicio.day:02d}/{meses_del_año.index(mes) + 1:02d}/24 - {fecha_viaje_fin.day:02d}/{meses_del_año.index(mes) + 1:02d}/24'

            estrellas_hotel = estrellas_por_hotel[hotel]

            if ciudad in viaje_montaña_provincias:
                tipo_exp = "Montaña"
            elif ciudad in viaje_cultural_provincias:
                tipo_exp = "Cultural"
            elif ciudad in viaje_rural_provincias:
                tipo_exp = "Rural"
            elif ciudad in viaje_islas_provincias:
                tipo_exp = "Islas"
            elif ciudad in viaje_playa_provincias:
                tipo_exp = "Playa"
            elif ciudad in viaje_gastronómico_provincias:
                tipo_exp = "Gastronómico"
            else:
                tipo_exp = None  

            num_plazas = 9

            datos_plazas.append((ciudad, mes, hotel, estrellas_hotel, tipo_exp, fecha_viaje, num_plazas))

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
            print("-------------------------------------------------------------\n"
                "Conexión establecida\n"
                "-------------------------------------------------------------")

            nombre_tabla_plazas = 'plazas_disponibles'

            columnas_plazas = ['Ciudad', 'Mes', 'Hotel', 'Estrellas_hotel', 'Tipo_exp','Fecha_viaje', 'Num_plazas']
            marcadores_plazas = ', '.join(['%s'] * len(columnas_plazas))
            consulta_plazas = f"INSERT INTO {nombre_tabla_plazas} ({', '.join(columnas_plazas)}) VALUES ({marcadores_plazas})"

            cursor_plazas = conexion.cursor()
            cursor_plazas.executemany(consulta_plazas, datos_plazas)
            conexion.commit()

            print(f"600 destinos insertados correctamente en la tabla '{nombre_tabla_plazas}' de la base de datos '{database}'")

    except Exception as e:
        print(f"Error desconocido: {e}")
    finally:
        if 'conexion' in locals() and conexion.open:
            conexion.close()
            print("-------------------------------------------------------------\n"
                "Conexión cerrada")