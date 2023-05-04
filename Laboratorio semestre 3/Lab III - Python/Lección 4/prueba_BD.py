import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) # Con esto ejecutamos la sentencia
registros = cursor.fetchall() # Esto recupera todos los registros de la sentencia
print(registros)

cursor.close()
conexion.close()