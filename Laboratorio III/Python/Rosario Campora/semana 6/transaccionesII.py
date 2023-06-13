from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Definir la clase base para las clases declarativas
Base = declarative_base()

# Definir la clase Persona como una clase declarativa
class Persona(Base):
    __tablename__ = 'persona'

    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)

# Clase para gestionar la transacción en la base de datos
class GestionarTransaccion:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def ejecutar_transaccion(self):
        engine = create_engine('postgresql://postgres:admin@localhost:5432/test_bd')
        Session = sessionmaker(bind=engine)

        try:
            session = Session()

            # Insertar un nuevo registro
            nueva_persona = Persona(nombre=self.nombre, apellido=self.apellido, email=self.email)
            session.add(nueva_persona)

            # Actualizar un registro existente
            persona_actualizar = session.query(Persona).filter_by(id_persona=1).first()
            if persona_actualizar:
                persona_actualizar.nombre = 'Roberto'
                persona_actualizar.apellido = 'Carlos'
                persona_actualizar.email = 'rcperez@mail.com'

            session.commit() # Realizar el commit para cerrar la transacción
            print('Termina la transacción')
        except Exception as e:
            session.rollback()
            print(f'Ocurrió un error, se hizo un rollback: {e}')
        finally:
            session.close()

# Crear una instancia de la clase GestionarTransaccion y ejecutar la transacción
gestionador = GestionarTransaccion('Jorge', 'Prol', 'jprol@mail.com')
gestionador.ejecutar_transaccion()
