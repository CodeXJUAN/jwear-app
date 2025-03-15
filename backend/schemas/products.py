from pydantic import BaseModel

class HomeBase(BaseModel):
    imagen_front: str
    imagen_back: str
    nombre_prod: str
    color: str
    precio: float

class HomeCreate(HomeBase):
    pass

class Home(HomeBase):
    id: int

    class Config:
        orm_mode = True

class OtherImagesBase(BaseModel):
    imagen: str
    nombre_img: str

class OtherImagesCreate(OtherImagesBase):
    pass

class OtherImages(OtherImagesBase):
    id: int

    class Config:
        orm_mode = True

class TshirtsBase(BaseModel):
    imagen_front: str
    imagen_back: str
    nombre_prod: str
    color: str
    precio: float

class TshirtsCreate(TshirtsBase):
    pass

class Tshirts(TshirtsBase):
    id: int

    class Config:
        orm_mode = True

class SweatersBase(BaseModel):
    imagen_front: str
    imagen_back: str
    nombre_prod: str
    color: str
    precio: float

class SweatersCreate(SweatersBase):
    pass

class Sweaters(SweatersBase):
    id: int

    class Config:
        orm_mode = True

class HoddiesBase(BaseModel):
    imagen_front: str
    imagen_back: str
    nombre_prod: str
    color: str
    precio: float

class HoddiesCreate(HoddiesBase):
    pass

class Hoddies(HoddiesBase):
    id: int

    class Config:
        orm_mode = True