from sqlalchemy import create_engine
import psycopg2
import logging
import pandas as pd
from dotenv import load_dotenv
import os

# obtengo información del archivo de configuración 

load_dotenv()

# configuración para registros de la DDBB
logging.basicConfig(filename='scripts/DDBB.log',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d - %m - %Y')

try:
    USER_NAME = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_NAME = os.getenv('POSTGRES_DB')
    HOST = os.getenv('POSTGRES_HOST')
    logging.info('Se extrajo la información del .env')
    
except Exception as e:
    logging.error(e)
    
def connect_DDBB(HOST,USER_NAME,PASSWORD,DB_NAME):
    #conexión a la DDBB
    try:
        engine = create_engine(f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:5432/{DB_NAME}")
        #query sencilla a la DDBB
        query_sql = 'SELECT * FROM USUARIOS'
        query_pd = pd.read_sql_query(query_sql, engine)
        logging.info('Conexión exitosa a la DDBB y se extrajo la query')
        logging.info(query_pd)
        
    except Exception as e:
        logging.error(e)

connect_DDBB(HOST,USER_NAME,PASSWORD,DB_NAME)
