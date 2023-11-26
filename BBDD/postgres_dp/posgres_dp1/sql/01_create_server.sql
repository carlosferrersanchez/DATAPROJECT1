-- En este ejemplo, se agrega un servidor llamado 'MyPostgresServer'

INSERT INTO pgadmin_servers (user_id, servergroup_id, name, host, port, maintenance_db, username, password)
VALUES (
    1, -- user_id (puede variar dependiendo de tu configuración)
    1, -- servergroup_id (puede variar dependiendo de tu configuración)
    'MyPostgresServer', -- nombre del servidor
    'postgres', -- host del servidor PostgreSQL (nombre del servicio en tu docker-compose)
    5432, -- puerto del servidor PostgreSQL
    'example-database', -- base de datos de mantenimiento
    'example-database', -- usuario
    'example-database-password' -- contraseña
);

