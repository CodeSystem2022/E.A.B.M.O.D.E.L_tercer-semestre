from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def consultar_personas():
    # Establecer la conexión con la base de datos
    engine = create_engine('postgresql://postgres:root@127.0.0.1:5432/test_db')
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Ejecutar la consulta utilizando SQLAlchemy
        registros = session.execute('SELECT * FROM persona').fetchall()
        print(registros)
    finally:
        # Cerrar la sesión
        session.close()

# Llamar a la función para ejecutar la consulta
consultar_personas()
