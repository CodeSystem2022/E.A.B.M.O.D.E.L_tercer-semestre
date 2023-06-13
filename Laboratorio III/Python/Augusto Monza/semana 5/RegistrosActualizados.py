import psycopg2

def actualizar_persona():
    # Conectarse a la base de datos
    conexion = psycopg2.connect(user='postgres', password='240484', host='127.0.0.1', port='5432', database='test_bd')
    
    try:
        with conexion:
            with conexion.cursor() as cursor:
                # Definir la sentencia SQL y los valores a actualizar
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1)
                
                # Ejecutar la sentencia SQL con los valores proporcionados
                cursor.execute(sentencia, valores)
                
                # Obtener el número de registros actualizados
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')

    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        # Cerrar la conexión a la base de datos
        conexion.close()

# Llamar a la función para realizar la actualización
actualizar_persona()
