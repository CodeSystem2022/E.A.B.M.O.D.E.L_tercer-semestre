-- Crear la secuencia
CREATE SEQUENCE IF NOT EXISTS persona_id_seq;

-- Crear la tabla "usuarios"
CREATE TABLE IF NOT EXISTS public.usuarios
(
    id_usuario integer NOT NULL DEFAULT nextval('persona_id_seq'),
    nombre_completo character varying COLLATE pg_catalog."default",
    apellido character varying COLLATE pg_catalog."default",
    correo_electronico character varying COLLATE pg_catalog."default",
    CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario)
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;

-- Insertar datos en la tabla "usuarios"
INSERT INTO usuarios(nombre_completo, apellido, correo_electronico) VALUES ('Ana López', 'García', 'ana.lopez@example.com');
INSERT INTO usuarios(nombre_completo, apellido, correo_electronico) VALUES ('Carlos Rodríguez', 'Martínez', 'carlos.rodriguez@example.com');

-- Seleccionar todas las filas de la tabla "usuarios"
SELECT * FROM usuarios;
