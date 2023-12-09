no hay personas NO españolas y NO residentes en españa

flujo --> 
1- install requirements
2- docker-compose up -d
3- conexion.py
4- plazas_disponibles.py
5- criba_bbdd
6- valoraciones.py
7- asignacion_plazas.py


Base de datos conectada y funcionando en localhost

Tenemos dos archivos de scripts, uno para cada sistema operativo, teniendo que lanzar uno dependiendo del entorno:
- Para entorno y Sistema Operativo macOS --> script.sh
        Para conectar:
          - cd Base de Datos
          - ./script.sh           
          - chmod +x script.sh (es posible que te pida permisos, si es asi con este comando te debería dejar, si te va a la primera no es necesario)
  
- Para entorno y Sistema Operativo Windowsa --> script.bat
        Para conectar:
          - cd Base de Datos
          - .\script.bat


Para entrar en la Base de Datos, habra que entrar al localhost:8080 , donde veremos como está phpMyAdmin lanzado y listo para introducir las credenciales

Las credenciales son:
- Usuario: user
- Contraseña: admin01