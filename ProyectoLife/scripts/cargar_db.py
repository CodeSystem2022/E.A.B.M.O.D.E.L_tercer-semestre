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
    from models.usuarios import Usuario, Base
    Base.metadata.create_all(engine)


if __name__== '__main__':
    # URL de los alimentos
    url_alimentos = "ProyectoLife/utils/db_alimentos.csv"

    # Creamos y cargamos la tabla alimentos
    lectura_tabla_alimentos(url_alimentos)

    # Crear tabla usuario
    crear_tabla_usuarios()
