from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()

class Facultad(Base):
    __tablename__ = 'facultades'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    decano = Column(String, nullable=False)
    
    carreras = relationship("Carrera", back_populates="facultad")

class Carrera(Base):
    __tablename__ = 'carreras'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo_interno = Column(String, unique=True, nullable=False)
    
    facultad_id = Column(Integer, ForeignKey('facultades.id'), nullable=False)
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

class Profesor(Base):
    __tablename__ = 'profesores'
    
    id = Column(Integer, primary_key=True)
    nombres_apellidos = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    especialidad = Column(String, nullable=False)
    
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    url = Column(String, nullable=False)
    
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    profesor = relationship("Profesor", back_populates="recursos")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("¡Tablas creadas con éxito!")