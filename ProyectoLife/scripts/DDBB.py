from sqlalchemy import create_engine
import logging
import pandas as pd
from dotenv import load_dotenv
import os

'''
Este archivo permite conectarse a la Base de Datos PostgreSQL
'''

def connect_DDBB():
    # obtengo información del archivo de configuración 
    load_dotenv()
    try:
        USER_NAME = os.getenv('POSTGRES_USER')
        PASSWORD = os.getenv('POSTGRES_PASSWORD')
        DB_NAME = os.getenv('POSTGRES_DB')
        HOST = os.getenv('POSTGRES_HOST')
        logging.info('Se extrajo la información del .env')
    
    except Exception as e:
        logging.error(e)

    #conexión a la DDBB
    try:
        engine = create_engine(f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:5432/{DB_NAME}")
        logging.info('Conexión exitosa a la DDBB')
        return engine
        
        
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    connect_DDBB()
