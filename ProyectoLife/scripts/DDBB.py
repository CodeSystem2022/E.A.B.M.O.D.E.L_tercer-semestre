from sqlalchemy import create_engine
import logging
import pandas as pd
from dotenv import load_dotenv
import os

# obtengo información del archivo de configuración 
path = 'E.A.B.M.O.D.E.L_tercer-semestre/ProyectoLife/.env'
load_dotenv(path)

# configuración para registros de la DDBB
logging.basicConfig(filename='E.A.B.M.O.D.E.L_tercer-semestre/ProyectoLife/scripts/DDBB.log',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d - %m - %Y')

try:
    USER_NAME = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_NAME = os.getenv('POSTGRES_DB')
    logging.info('Se extrajo la información del .env')
    
except Exception as e:
    logging.error(e)
    
def connect_DDBB(USER_NAME,PASSWORD,DB_NAME):
    #conexión a la DDBB
    try:
        engine = create_engine(f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@0.0.0.0:5431/{DB_NAME}')
        
        #query sencilla a la DDBB
        query_sql = 'SELECT * FROM USUARIOS'
        query_pd = pd.read_sql_query(query_sql, engine)
        logging.info('Conexión exitosa a la DDBB y se extrajo la query')
        logging.info(query_pd)
        
    except Exception as e:
        logging.error(e)

connect_DDBB(USER_NAME,PASSWORD,DB_NAME)