from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'

    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)

def actualizar_persona():
    # Establecer la conexión con la base de datos
    engine = create_engine('postgresql://postgres:240484@127.0.0.1:5432/test_bd')
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Realizar la actualización utilizando SQLAlchemy
        persona = session.query(Persona).filter_by(id_persona=1).first()
        if persona:
            persona.nombre = 'Juan Carlos'
            persona.apellido = 'Roldan'
            persona.email = 'rcarlos@mail.com'
            session.commit()
            print('La persona se ha actualizado correctamente')
        else:
            print('No se encontró la persona con el ID especificado')
    except Exception as e:
        print(f'Ocurrió un error durante la actualización: {e}')
        session.rollback()
    finally:
        # Cerrar la sesión
        session.close()

# Llamar a la función para realizar la actualización
actualizar_persona()
