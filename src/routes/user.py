from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas
from ..controllers import user

router=APIRouter(      
       prefix='/user/products',
       tags=['User'])

@router.post('/',status_code=status.HTTP_201_CREATED)
def new_user(req:schemas.User_creation,db: Session=Depends(database.get_db)):
    return user.create_user(req,db)

@router.get('/', status_code=status.HTTP_200_OK)
def all_products(db:Session=Depends(database.get_db)):
    return user.all(db)

@router.get('/{id}')
def show_1_product(id,db:Session=Depends(database.get_db)):
    return user.show_1(id,db)