from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas
from ..controllers import admin

router=APIRouter(      
       prefix='/admin/products',
       tags=['Admin'])

@router.get('/{id}')
def show_1_product(id,db:Session=Depends(database.get_db)):
    return admin.show_1(id,db)

@router.get('/', status_code=status.HTTP_200_OK)
def all_products(db:Session=Depends(database.get_db)):
    return admin.all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def add_product(req:schemas.Products,db:Session=Depends(database.get_db)):
    return admin.add_product(req,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_product(id,req:schemas.Products,db:Session=Depends(database.get_db)):
    return admin.update(id,req,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id,db:Session=Depends(database.get_db)):
    return admin.destroy(id,db)


