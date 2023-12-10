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



DP:
    /python
        launcher.py
        /scripts.py
        dockerfile
    /mysql
        docker-compose
        dockerfile
        create_tables.sql
    docker-compose.yml