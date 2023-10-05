from typing import Optional
from pydantic import BaseModel

class AlbumsM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]

class ArtistsM(BaseModel):
    # id: Optional[int]
    title: str
    short_name: str

class GenresM(BaseModel):
    # id: Optional[int]
    product_type: str
    note: Optional[str]

class SongsM(BaseModel):
    # id: Optional[int]
    left_in_stock: int
    note: Optional[str]

class CustomersM(BaseModel):
    # id: Optional[int]
    user_id: int

class OrdersM(BaseModel):
    # transaction_code: Optional[int]
    online_magazine_id: int
    user_id: int
    product_id: int
    manager_id: int
    date_and_time_of_receipt: str
    title: Optional[str]

class OrderDetailsM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]

class EmployeesM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]

class PublishersM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]

class CopyrightsM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]