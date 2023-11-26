

-- TABLA PERSONAS

create table if not exists personas (
    id_persona int not null,
    nombre varchar(50) not null,
    apellido1 varchar(50) not null,
    apellido2 varchar(50) not null,
    DNI varchar(50) not null,
    telefono int not null,
    fecha_nacimiento DATE not null,
    nacionalidad varchar(50) not null,
    pais_residencia varchar(50) not null,
    provincia varchar(50) not null,
    estado_civil varchar(50) not null,
    tiene_pareja boolean not null,
    num_hijos int not null,
    hijo_discapacidad boolean not null,
    personas_dependientes int not null,
    discapacidad boolean not null,
    tipo_discapacidad varchar(50),
    grado_discapacidad int,
    num_viajes_previos int not null,
    renta int not null,
    pensionista boolean not null,
    obras_sociales int not null,
    preferencia_destino varchar(50) not null,
    preferencia_fecha varchar(50) not null,
    constraint pk_persona primary key (id_persona)
);

-- TABLA HOTELES

create table if not exists destinos (
    id_destino int not null,
    hotel varchar(50) not null,
    ciudad varchar(50) not null,
    zona_destino varchar(50) not null,
    fecha_viaje DATE not null,
    constraint pk_destino primary key (id_destino)
);











