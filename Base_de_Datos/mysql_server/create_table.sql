-- DROP TABLE IF EXISTS
DROP TABLE IF EXISTS personas;
DROP TABLE IF EXISTS destinos;

-- TABLA PERSONAS

CREATE TABLE IF NOT EXISTS personas (
    id_persona INT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Primer_apellido VARCHAR(50) NOT NULL,
    Segundo_apellido VARCHAR(50) NOT NULL,
    Sexo VARCHAR(50) NOT NULL,
    Nacionalidad VARCHAR(50) NOT NULL,
    DNI VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    Pais_residencia VARCHAR(10000) NOT NULL,
    Fecha_nacimiento DATE NOT NULL,
    Edad INT NOT NULL,
    Provincia VARCHAR(50) NOT NULL,
    Estado_civil VARCHAR(50) NOT NULL,
    Acompanamiento_pareja BOOLEAN NOT NULL,
    Hijo_discapacidad BOOLEAN NOT NULL,
    Discapacidad BOOLEAN NOT NULL,
    Tipo_discapacidad VARCHAR(50),
    Grado_discapacidad INT,
    Numero_participaciones INT,
    Renta INT NOT NULL,
    Personas_dependientes INT,
    Pension VARCHAR(50),
    Obras_sociales VARCHAR(50) NOT NULL,
    Vive_solo BOOLEAN NOT NULL,
    CONSTRAINT pk_persona PRIMARY KEY (id_persona)
);

-- TABLA DESTINOS

CREATE TABLE IF NOT EXISTS destinos (
    id_destino INT NOT NULL AUTO_INCREMENT,
    hotel VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    zona_destino VARCHAR(50) NOT NULL,
    fecha_viaje DATE NOT NULL,
    CONSTRAINT pk_destino PRIMARY KEY (id_destino)
);








