from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from scripts.cargar_db import conexion_db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    contraseña = Column(String(255), nullable=False)
    confir_contraseña = Column(String(255), nullable=False)
