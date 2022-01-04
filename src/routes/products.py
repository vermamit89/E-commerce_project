from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas

router=APIRouter(      
       prefix='/products',
       tags=['Products'])




# @router.get('/', status_code=status.HTTP_200_OK)
# def all(db:Session=Depends(database.get_db)):
#     products=db.query(models.Product).all()
#     return products

# @router.get('/{id}')
# def show_1(id,db:Session=Depends(database.get_db)):
#     product_1=db.query(models.Product).filter(models.Product.id==id).first()
#     if not product_1:
#         raise HTTPException(status_code=404,detail=f'product with the id {id} not found')

#     return product_1

