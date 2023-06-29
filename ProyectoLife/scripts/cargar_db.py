import sys
import os
import pandas as pd
from sqlalchemy import create_engine
from DDBB import get_db

# Agregar el directorio raíz del proyecto a la ruta de búsqueda de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Creamos otra conexión para cargados de manera descentralizada de la base de datos
def conexion_db():
    engine = create_engine(get_db())
    return engine


def lectura_tabla_alimentos(url):
    # Leemos con pandas el csv
    df = pd.read_csv(url, sep=',' , encoding='utf-8')
    engine = conexion_db()

    df.to_sql("alimentos", engine, if_exists='replace', index=False)

def crear_tabla_usuarios():
    engine = conexion_db()
    from models.models import Usuario, Base
    Base.metadata.create_all(engine)

def crear_tabla_imc():
    engine = conexion_db()
    from models.models import Imc, Base
    Base.metadata.create_all(engine)


def crear_calorias_quemadas():
    engine = conexion_db()
    from models.models import CaloriasQuemadas, Base
    Base.metadata.create_all(engine)


def crear_peso_ideal():
    engine = conexion_db()
    from models.models import PesoIdeal, Base
    Base.metadata.create_all(engine)


if __name__== '__main__':
    try:
        # URL de los alimentos
        url_alimentos = "utils/db_alimentos.csv"

        # Creamos y cargamos la tabla alimentos
        lectura_tabla_alimentos(url_alimentos)

        # Crear tabla usuario
        crear_tabla_usuarios()

        # Crear tabla imc
        crear_tabla_imc()

        # Crear tabla calorias quemadas
        crear_calorias_quemadas()

        # Crear tabla peso ideal
        crear_peso_ideal()

        print("Base de datos creada y cargada correctamente")
    except Exception as e:
        print("Error al crear la base de datos: ", e)


