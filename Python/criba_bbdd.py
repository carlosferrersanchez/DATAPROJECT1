import pymysql

hostname = '127.0.0.1'
database = 'mi_base_de_datos'
username = 'user'
password = 'admin01'

# Funciones para las características excluyentes #
        # NO españoles que NO residan en España
        # SI españoles que NO reciban algun tipo de pensión
        # Pensionistas de viudedad de menos de 55 años
        # Desempleados / Otro tipo de pensionistas de menos de 60 años
        # Beneficiario de la SS menores de 65 años

def no_espanoles_fuera_espana(cursor):
    consulta = "DELETE FROM personas WHERE Nacionalidad != 'España' AND Pais_residencia != 'España'"
    cursor.execute(consulta)

def españoles_sin_pension(cursor):
    consulta = "DELETE FROM personas WHERE nacionalidad = 'España' AND Pension != 'Titular SS' AND Pension != 'Desempleo/Otros subsidios' AND Pension != 'Jubilacion' AND Pension != 'Viuedad' AND Pension != 'Extranjero'"
    cursor.execute(consulta)

def pension_viudedad_menor_55(cursor):
    consulta = "DELETE FROM personas WHERE Pension = 'Viudead' AND EDAD < 55"
    cursor.execute(consulta)

def desempleados_menor_60(cursor):
    consulta = "DELETE FROM personas WHERE Pension = 'Desempleo/Otros subsidios' AND EDAD < 60"
    cursor.execute(consulta)

def beneficiarios_ss_menores_65(cursor):
    consulta = "DELETE FROM personas WHERE Pension = 'Titular SS' AND EDAD < 65"
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
        no_espanoles_fuera_espana(cursor)
        españoles_sin_pension(cursor)
        pension_viudedad_menor_55(cursor)
        desempleados_menor_60(cursor)
        beneficiarios_ss_menores_65(cursor)

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
