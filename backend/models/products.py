from sqlalchemy import Column, Integer, String, DECIMAL
from ..database import Base

class HOME(Base):
    __tablename__ = "HOME"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    IMAGEN_FRONT = Column(String, nullable=False)
    IMAGEN_BACK = Column(String, nullable=False)
    NOMBRE_PROD = Column(String, nullable=False)    
    COLOR = Column(String, nullable=False) 
    PRECIO = Column(DECIMAL, nullable=False)

class OTHER_IMAGES(Base):
    __tablename__ = "OTHER_IMAGES"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    IMAGEN = Column(String, nullable=False)
    NOMBRE_IMG = Column(String, nullable=False)

class TSHIRTS(Base):
    __tablename__ = "TSHIRTS"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    IMAGEN_FRONT = Column(String, nullable=False)
    IMAGEN_BACK = Column(String, nullable=False)
    NOMBRE_PROD = Column(String, nullable=False)    
    COLOR = Column(String, nullable=False) 
    PRECIO = Column(DECIMAL, nullable=False)

class SWEATERS(Base):
    __tablename__ = "SWEATERS"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    IMAGEN_FRONT = Column(String, nullable=False)
    IMAGEN_BACK = Column(String, nullable=False)
    NOMBRE_PROD = Column(String, nullable=False)    
    COLOR = Column(String, nullable=False) 
    PRECIO = Column(DECIMAL, nullable=False)

class HODDIES(Base):
    __tablename__ = "HODDIES"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    IMAGEN_FRONT = Column(String, nullable=False)
    IMAGEN_BACK = Column(String, nullable=False)
    NOMBRE_PROD = Column(String, nullable=False)    
    COLOR = Column(String, nullable=False) 
    PRECIO = Column(DECIMAL, nullable=False)