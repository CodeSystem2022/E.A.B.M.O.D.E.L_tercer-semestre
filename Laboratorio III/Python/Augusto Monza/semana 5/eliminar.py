import psycopg2

class GestorBaseDatos:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.conexion = None

    def conectar(self):
        self.conexion = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                         database=self.database)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()

    def eliminar_registro(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    sentencia = 'DELETE FROM persona WHERE id_persona=%s'
                    entrada = input('Digite el número de registro a eliminar: ')
                    valores = (entrada,) # es una tupla de valores
                    cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
                    registros_eliminados = cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')
        except Exception as e:
            print(f'Ocurrió un error: {e}')

# Crear una instancia de la clase GestorBaseDatos y realizar la eliminación de registros
gestor_bd = GestorBaseDatos(user='postgres', password='240484', host='127.0.0.1', port='5432', database='test_bd')
gestor_bd.conectar()
gestor_bd.eliminar_registro()
gestor_bd.desconectar()
