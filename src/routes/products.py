from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas

router=APIRouter(      
       prefix='/products',
       tags=['Products'])


@router.post('/',status_code=status.HTTP_201_CREATED)
def add_product(req:schemas.Products,db:Session=Depends(database.get_db)):
    new_product=models.Product(product_name=req.p_name, mrp=req.mrp , discounted_price=req.discounted_price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get('/', status_code=status.HTTP_200_OK)
def all(db:Session=Depends(database.get_db)):
    products=db.query(models.Product).all()
    return products