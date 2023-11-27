Base de datos en DBeaver de mysql

Hay que conectarlo manualmente

Para iniciar:
    - docker-compose up -d
    - Abrir un visualizador, en este caso DBeaver
    - Conectar al Servidor:
      - Url: jdbc:mysql://localhost:3306/mi_base_de_datos?allowPublicKeyRetrieval=true
      - MYSQL_USER: user
      - MYSQL_PASSWORD: admin01