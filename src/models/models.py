from sqlalchemy import Column,Integer,String,Boolean, Float


from . database import base


class User(base):
    __tablename__='User'

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    mobile=Column(Integer)
    isVerified=Column(Boolean)
    uniqueId=Column(String)

class Product(base):
    __tablename__='Products'

    id=Column(Integer,primary_key=True,index=True)
    product_name=Column(String)
    mrp= Column(Float)

    
    


