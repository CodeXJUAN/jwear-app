from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/home", response_model=schemas.Home)
def create_home_product(product: schemas.HomeCreate, db: Session = Depends(database.get_db)):
    db_product = models.HOME(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/home/{product_id}", response_model=schemas.Home)
def read_home_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = db.query(models.HOME).filter(models.HOME.ID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/other_images", response_model=schemas.OtherImages)
def create_other_image(image: schemas.OtherImagesCreate, db: Session = Depends(database.get_db)):
    db_image = models.OTHER_IMAGES(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@router.get("/other_images/{image_id}", response_model=schemas.OtherImages)
def read_other_image(image_id: int, db: Session = Depends(database.get_db)):
    db_image = db.query(models.OTHER_IMAGES).filter(models.OTHER_IMAGES.ID == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.post("/tshirts", response_model=schemas.Tshirts)
def create_tshirt_product(product: schemas.TshirtsCreate, db: Session = Depends(database.get_db)):
    db_product = models.TSHIRTS(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/tshirts/{product_id}", response_model=schemas.Tshirts)
def read_tshirt_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = db.query(models.TSHIRTS).filter(models.TSHIRTS.ID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/sweaters", response_model=schemas.Sweaters)
def create_sweater_product(product: schemas.SweatersCreate, db: Session = Depends(database.get_db)):
    db_product = models.SWEATERS(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/sweaters/{product_id}", response_model=schemas.Sweaters)
def read_sweater_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = db.query(models.SWEATERS).filter(models.SWEATERS.ID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/hoddies", response_model=schemas.Hoddies)
def create_hoddie_product(product: schemas.HoddiesCreate, db: Session = Depends(database.get_db)):
    db_product = models.HODDIES(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/hoddies/{product_id}", response_model=schemas.Hoddies)
def read_hoddie_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = db.query(models.HODDIES).filter(models.HODDIES.ID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product