import psycopg2

conexion_sin_bd = psycopg2.connect(
    user="tu_usuario",
    password="tu_contraseña",
    host="localhost",
    port="5432"
)

# Crear un objeto cursor para ejecutar comandos SQL
cursor_sin_bd = conexion_sin_bd.cursor()

# Crear una nueva base de datos
nombre_base_datos = "DataProject1"
consulta_creacion_bd = f"CREATE DATABASE {nombre_base_datos};"
cursor_sin_bd.execute(consulta_creacion_bd)

# Confirmar la transacción y cerrar la conexión sin base de datos
conexion_sin_bd.commit()
conexion_sin_bd.close()

print(f"La base de datos '{nombre_base_datos}' ha sido creada exitosamente.")

# Establecer la conexión con la nueva base de datos
conexion = psycopg2.connect(
    database=nombre_base_datos,
    user="admin",
    password="dataproject1",
    host="localhost",
    port="5432"
)

# Crear un objeto cursor para ejecutar comandos SQL en la nueva base de datos
cursor = conexion.cursor()

# Aquí puedes realizar otras operaciones en la base de datos si es necesario

# Confirmar la transacción y cerrar la conexión con la nueva base de datos
conexion.commit()
conexion.close()