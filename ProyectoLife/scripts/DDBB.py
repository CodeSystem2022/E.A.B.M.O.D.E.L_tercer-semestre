from flask_sqlalchemy import SQLAlchemy
import logging
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

'''
Este archivo permite conectarse a la Base de Datos PostgreSQL
'''

# Varaibles globales

USER_NAME = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
HOST = os.getenv('POSTGRES_HOST')


def get_db():
    # si el entorno es local primero debo tener activo el proxy SQL de GCP
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:5432/{DB_NAME}"
    logging.info('Conexión exitosa a la DDBB')
    return SQLALCHEMY_DATABASE_URI


if __name__ == '__main__':
    get_db()
