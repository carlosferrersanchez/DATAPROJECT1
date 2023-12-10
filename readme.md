flujo --> 
1- install requirements
2- docker-compose up -d
3- personas.py
4- plazas_disponibles.py
5- criba_bbdd
6- valoraciones.py
7- asignacion_plazas.py


Para entrar en la Base de Datos, habra que entrar al localhost:8080 , donde veremos como está phpMyAdmin lanzado y listo para introducir las credenciales

Las credenciales son:
- Usuario: user
- Contraseña: admin01


DESCRIPCIÓN DEL PROYECTO

El Instituto de Mayores y Servicios Sociales quiere mejorar y renovar el sistema de asignación de plazas en su programa turístico. Para ello, el objetivo de nuestro programa, Forever Young, es asignar la totalidad de plazas disponibles para el año 2024 de una manera justa y equitativa, teniendo en cuenta indicadores como la renta económica, edad, participaciones anteriores, aislamiento social, colaboración en obras sociales, entre otros. Además, nuestro modelo tendrá en cuenta para la asignación de plazas, las preferencias de las personas solicitantes en función de la experiencia viajera que cada uno de ellos elijan. 

DISEÑO DE LA ARQUITECTURA

En nuestro proyecto existen 3 contenedores Docker, encargados del proceso de Extracción, Transformación y Carga:

1. Contenedor Python, responsable tanto de la extracción como de la transformación de los datos. Se encarga de la creación de las diferentes bases de datos: 
   
  - Personas Inscritas
  - Destinos disponibles

Una vez obtenida la lista de personas inscritas realiza la criba para obtener las personas admitidas. A partir de entonces, se encarga de llevar a cabo la atribución de puntos en función de las variables determinantes en nuestro proyecto, obteniendo así un orden de prioridad de todas las personas admitidas en éste y relacionándolas con los destinos disponibles para obtener las siguientes bases de datos:

   - Viajes asignados
   - Lista de espera

Finalmente, también se encarga de cargar los datos en las tablas de la base de datos SQL.

2. Contenedor MySQL, encargado de almacenar la base de datos del proyecto. Creamos las tablas a partir de un archivo .sql que serán posteriormente rellenadas por un script de python.
   
3. Contenedor phpMyAdmin, que falicita la administración de la base de datos del proyecto a través de una interfaz web.
   
4. Contenedor Jupyter - falta

Diagrama con la arquitectura:

Foto aquí

En cuanto a nuestro modelo de datos, contamos con 4 tablas: Personas, Destinos, Viajes asignados y Lista de espera. Explicar tablas.

Foto modelo de datos

EJECUCIÓN DEL RPOYECTO

