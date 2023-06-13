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

class GestorBaseDatos:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:admin@localhost:5432/test_bd')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insertar_persona(self, nombre, apellido, email):
        try:
            persona = Persona(nombre=nombre, apellido=apellido, email=email)
            self.session.add(persona)
            self.session.commit()
            print('El registro se insertó correctamente')
        except Exception as e:
            self.session.rollback()
            print(f'Ocurrió un error durante la inserción: {e}')
        finally:
            self.session.close()

# Crear una instancia de la clase GestorBaseDatos y realizar la inserción de una persona
gestor_bd = GestorBaseDatos()
gestor_bd.insertar_persona('Maria', 'Esperanza', 'mesperanza@mail.com')
