from pydantic import BaseModel

class User_creation(BaseModel):
    name:str
    email: str
    password: str
    mobile:str

class Products(BaseModel):
    p_name: str
    mrp : float
    discounted_price : float