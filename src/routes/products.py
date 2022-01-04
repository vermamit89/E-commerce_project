from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas

router=APIRouter(      
       prefix='/products',
       tags=['Products'])


@router.post('/',status_code=status.HTTP_201_CREATED)
def creat_blog(req:schemas.Products,db:Session=Depends(database.get_db)):
    new_product=models.Product(req)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product