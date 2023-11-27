from conexion import hostname, database, username, password

# Obtén los parámetros del usuario y la contraseña desde la URL
usuario = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")

try:
    conexion = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    if conexion.is_connected():
        print("Conexión establecida")

        # Prepara la consulta SQL con parámetros
        consulta = "SELECT * FROM jefeclinico WHERE usuario=%s AND password=%s"
        valores = (usuario, password)

        with conexion.cursor(dictionary=True) as cursor:
            # Ejecuta la consulta SQL con los parámetros
            cursor.execute(consulta, valores)

            # Obtiene el resultado como un diccionario
            resultado = cursor.fetchone()

            if resultado:
                # Imprime el resultado como JSON
                print(json.dumps(resultado, ensure_ascii=False))
            else:
                print("Usuario y/o contraseña incorrectos.")

except mysql.connector.Error as e:
    print(f"No se ha podido establecer conexión: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")