-- consulta de informacion seleccionada
SELECT * FROM persona WHERE id_persona IN (1,2,3)

-- ingresamos un nuevo elemento a la tabla
INSERT INTO persona(nombre, apellido, email) VALUES ('Pedro','Gonzalez', 'pgon@gmail.com')

-- hacemos la consulta para ver toda la informacion de la tabla
SELECT * FROM persona

-- actualizar los datos
UPDATE persona SET nombre = 'Maria', apellido = 'Perez', email = 'Mperez@mail.com'

-- consultar toda la informacion de la tabla

SELECT * FROM persona

-- Eliminamos una persona de la tabla
DELETE FROM persona WHERE id_persona = 3