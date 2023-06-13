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
        self.engine = create_engine('postgresql://postgres:240484@localhost:5432/test_bd')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def eliminar_registro(self, id_persona):
        try:
            persona = self.session.query(Persona).get(id_persona)
            if persona:
                self.session.delete(persona)
                self.session.commit()
                print('El registro ha sido eliminado correctamente')
            else:
                print('No se encontró la persona con el ID especificado')
        except Exception as e:
            print(f'Ocurrió un error durante la eliminación: {e}')
            self.session.rollback()
        finally:
            self.session.close()

# Crear una instancia de la clase GestorBaseDatos y realizar la eliminación de registros
gestor_bd = GestorBaseDatos()
gestor_bd.eliminar_registro(1)  # Proporciona el ID de la persona a eliminar
