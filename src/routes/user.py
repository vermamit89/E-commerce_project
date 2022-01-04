from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from .. models import database, models , schemas

router=APIRouter(      
       prefix='/user/products',
       tags=['User'])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(req:schemas.User_creation,db: Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==req.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User record already exist!!!')
    new_user=models.User(username=req.name,email=req.email,password=req.password,
                                mobile=req.mobile,isVerified=False,uniqueId=100)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/', status_code=status.HTTP_200_OK)
def all(db:Session=Depends(database.get_db)):
    products=db.query(models.Product).all()
    return products

@router.get('/{id}')
def show_1(id,db:Session=Depends(database.get_db)):
    product_1=db.query(models.Product).filter(models.Product.id==id).first()
    if not product_1:
        raise HTTPException(status_code=404,detail=f'product with the id {id} not found')

    return product_1