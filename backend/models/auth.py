from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from passlib.context import CryptContext
from ..database import Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "USUARIOS"

    ID_USUARIO = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    NOMBRE = Column(String, nullable=False)
    APELLIDO = Column(String, nullable=False)
    EMAIL = Column(String, nullable=False, unique=True, index=True)
    CONTRASEÑA = Column(String, nullable=False)
    FECHA_DE_CREACION = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)