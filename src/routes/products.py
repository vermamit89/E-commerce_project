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

@router.get('/{id}')
def show_1(id,db:Session=Depends(database.get_db)):
    product_1=db.query(models.Product).filter(models.Product.id==id).first()
    if not product_1:
        raise HTTPException(status_code=404,detail=f'product with the id {id} not found')

    return product_1

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(database.get_db)):
    product_delete=db.query(models.Product).filter(models.Product.id==id)
    if not product_delete.first():
        raise HTTPException(status_code=404, detail=f'product with the id {id} not found to delete')
    product_delete.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'