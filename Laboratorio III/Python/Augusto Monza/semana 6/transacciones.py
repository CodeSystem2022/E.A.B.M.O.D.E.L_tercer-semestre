import psycopg2 as bd

def insertar_persona(nombre, apellido, email):
    try:
        conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
        cursor = conexion.cursor()
        sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
        valores = (nombre, apellido, email)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print('El registro se insertó correctamente')
    except Exception as e:
        conexion.rollback()
        print(f'Ocurrió un error, se hizo un rollback: {e}')
    finally:
        if conexion is not None:
            conexion.close()

# Llamar a la función para insertar una persona
insertar_persona('Maria', 'Esperanza', 'mesperanza@mail.com')
