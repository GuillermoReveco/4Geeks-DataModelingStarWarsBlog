import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellidos = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    children = relationship("Favoritopla")
    children = relationship("Favoritoper")

    def serialize(self):
        return{
            "id" : id.self,
            "nombre" : nombre.self,
            "apellidos" : apellidos.self,
            "email" : email.self,
            "password" : password.self
        }

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    rutaimagen = Column(String(250))
    habitantes = Column(Integer, nullable=False)
    terreno = Column(String(250), nullable=False)
    clima = Column(String(100), nullable=False)
    periodoOrbita = Column(Integer, nullable=False)
    periodoRotacion = Column(Integer, nullable=False)
    diametro = Column(Integer, nullable=False)
    children = relationship("Favoritopla")

    def serialize(self):
        return{
            "id" : id.self,
            "nombre" : nombre.self,
            "rutaimagen" : rutaimagen.self,
            "habitantes" : habitantes.self,
            "terreno" : terreno.self,
            "clima" : clima.self,
            "periodoOrbita" : periodoOrbita.self,
            "periodoRotacion" : periodoRotacion.self,
            "diametro" : diametro.self
        }

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    rutaimagen = Column(String(250))
    genero = Column(String(10), nullable=False)
    colorpelo = Column(String(20), nullable=False)
    colorojos = Column(String(20), nullable=False)
    nacimiento = Column(String(100), nullable=False)
    altura = Column(Integer, nullable=False)
    colorpiel = Column(String(20), nullable=False)
    children = relationship("Favoritoper")

    def serialize(self):
        return{
            "id" : id.self,
            "nombre" : nombre.self,
            "rutaimagen" : rutaimagen.self,
            "genero" : genero.self,
            "colorpelo" : colorpelo.self,
            "colorojos" : colorojos.self,
            "nacimiento" : nacimiento.self,
            "altura" : altura.self,
            "colorpiel" : colorpiel.self
        }

class Favoritoper(Base):
    __tablename__ = 'favoritoper'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), primary_key=True)

    def serialize(self):
        return{
            "usuario_id" : usuario_id.self,
            "personaje_id" : personaje_id.self
        }

class Favoritopla(Base):
    __tablename__ = 'favoritopla'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), primary_key=True)

    def serialize(self):
        return{
            "usuario_id" : usuario_id.self,
            "planeta_id" : planeta_id.self
        }



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')