from fastapi import Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas

def show_1(id,db:Session=Depends(database.get_db)): 
    product_1=db.query(models.Product).filter(models.Product.id==id).first()
    if not product_1:
        raise HTTPException(status_code=404,detail=f'product with the id {id} not found')
    return product_1


def all(db:Session=Depends(database.get_db)):
    products=db.query(models.Product).all()
    return products

def add_product(req:schemas.Products,db:Session=Depends(database.get_db)):
    new_product=models.Product(product_name=req.product_name, mrp=req.mrp , discounted_price=req.discounted_price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update(id,req:schemas.Products,db:Session=Depends(database.get_db)):
    product_update=db.query(models.Product).filter(models.Product.id==id)
    if not product_update.first():
        raise HTTPException(status_code=404, detail=f'product with the id {id} not found to update') 
    product_update.update(req.dict())
    db.commit()
    return 'updated'

def destroy(id,db:Session=Depends(database.get_db)):
    product_delete=db.query(models.Product).filter(models.Product.id==id)
    if not product_delete.first():
        raise HTTPException(status_code=404, detail=f'product with the id {id} not found to delete')
    product_delete.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'