-- Crea la secuencia
CREATE SEQUENCE IF NOT EXISTS persona_id_seq;

-- Crea la tabla persona
CREATE TABLE IF NOT EXISTS public.persona
(
    id_persona integer NOT NULL DEFAULT nextval('persona_id_seq'),
    nombre character varying COLLATE pg_catalog."default",
    apellido character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    CONSTRAINT persona_pkey PRIMARY KEY (id_persona)
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.persona
    OWNER to postgres;

-- Inserta datos en la tabla persona
INSERT INTO persona(nombre, apellido, email) VALUES ('Juan', 'Pérez', 'jperez@mail.com');
INSERT INTO persona(nombre, apellido, email) VALUES ('María', 'González', 'mgonzalez@mail.com');

-- Selecciona todas las filas de la tabla persona
SELECT * FROM persona;
