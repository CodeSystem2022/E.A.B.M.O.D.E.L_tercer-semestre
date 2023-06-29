from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
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
    
    imcs = relationship("Imc", back_populates="usuario")  # Define the one-to-many relationship

class Imc(Base):
    __tablename__ = 'imc'
    id = Column(Integer, primary_key=True)
    # ID usuario foreign de la tabla usuarios
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    sexo = Column(String(50), nullable=False)
    # edad en formato DATE
    edad = Column(Date, nullable=False)
    altura = Column(Integer, nullable=False)
    peso = Column(Integer, nullable=False)
    imc = Column(Float, nullable=False)
    dia_semana = Column(Integer, nullable=False)
    
    usuario = relationship("Usuario", back_populates="imcs")  # Define the many-to-one relationship


class CaloriasQuemadas(Base):
    __tablename__ = 'calorias_quemadas'
    id = Column(Integer, primary_key=True)
    # ID usuario foreign de la tabla usuarios
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    sexo = Column(String(50), nullable=False)
    # edad en formato DATE
    edad = Column(Date, nullable=False)
    altura = Column(Integer, nullable=False)
    peso = Column(Integer, nullable=False)
    actividad = Column(Float, nullable=False)
    calorias_quemadas = Column(Float, nullable=False)
    dia_semana = Column(Integer, nullable=False)

    usuario = relationship("Usuario", back_populates="calorias_quemadas")  # Define the many-to-one relationship


class PesoIdeal(Base):
    __tablename__ = 'peso_ideal'
    id = Column(Integer, primary_key=True)
    # ID usuario foreign de la tabla usuarios
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    sexo = Column(String(50), nullable=False)
    # edad en formato DATE
    edad = Column(Date, nullable=False)
    altura = Column(Integer, nullable=False)
    peso_ideal = Column(Float, nullable=False)

    usuario = relationship("Usuario", back_populates="peso_ideal")  # Define the many-to-one relationship

    
