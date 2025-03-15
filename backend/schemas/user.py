from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    nombre: str
    apellido: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id_usuario: int
    fecha_de_creacion: str

    class Config:
        orm_mode = True