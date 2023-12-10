import pymysql

def criba():
    hostname = 'mysql_server'
    database = 'imserso_database'
    username = 'user'
    password = 'admin01'

    def no_espanoles_fuera_espana(cursor):
        consulta = "DELETE FROM personas WHERE Nacionalidad != 'España' AND Pais_residencia != 'España'"
        cursor.execute(consulta)

    def españoles_sin_pension(cursor):
        consulta = "DELETE FROM personas WHERE nacionalidad = 'España' AND Pension != 'Titular SS' AND Pension != 'Desempleo/Otros subsidios' AND Pension != 'Jubilacion' AND Pension != 'Viuedad' AND Pension != 'Extranjero'"
        cursor.execute(consulta)

    def pension_viudedad_menor_55(cursor):
        consulta = "DELETE FROM personas WHERE Pension = 'Viuedad' AND EDAD < 55"
        cursor.execute(consulta)

    def desempleados_menor_60(cursor):
        consulta = "DELETE FROM personas WHERE Pension = 'Desempleo/Otros subsidios' AND EDAD < 60"
        cursor.execute(consulta)

    def beneficiarios_ss_menores_65(cursor):
        consulta = "DELETE FROM personas WHERE Pension = 'Titular SS' AND EDAD < 65"
        cursor.execute(consulta)

    def personas_multiples_discapacidades(cursor):
        consulta = "DELETE FROM personas WHERE grado_discapacidad > 2"
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

            no_espanoles_fuera_espana(cursor)
            españoles_sin_pension(cursor)
            pension_viudedad_menor_55(cursor)
            desempleados_menor_60(cursor)
            beneficiarios_ss_menores_65(cursor)
            personas_multiples_discapacidades(cursor)

            conexion.commit()

            print("Personas eliminadas según las características excluyentes")

            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
        conexion.rollback()

    finally:
        if 'conexion' in locals() and conexion.open:
            conexion.close()
