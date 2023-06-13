-- Consulta de información seleccionada
SELECT * FROM persona WHERE id_persona IN (1,2,3)

-- Ingresamos un nuevo elemento a la tabla
INSERT INTO persona(nombre, apellido, email) VALUES ('Pedro', 'González', 'pgonzalez@mail.com')

-- Hacemos la consulta para ver toda la información de la tabla
SELECT * FROM persona

-- Actualizamos los datos de una persona
UPDATE persona SET nombre = 'María', apellido = 'Pérez', email = 'mperez@mail.com' WHERE id_persona = 3

-- Consulta de toda la información de la tabla
SELECT * FROM persona

-- Eliminamos una persona de la tabla
DELETE FROM persona WHERE id_persona = 3
