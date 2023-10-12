from typing import Optional
from pydantic import BaseModel
from datetime import date

class AlbumsM(BaseModel):
    # album_id: int
    title: str
    artist_id: int
    release_date: date
    genre_id: int

class ArtistsM(BaseModel):
    # artist_id: int
    name: str
    country: str
    active_years: str

class GenresM(BaseModel):
    # genre_id: int
    name: str

class SongsM(BaseModel):
    # song_id: int
    title: str
    album_id: int
    artist_id: int
    duration: str

class CustomersM(BaseModel):
    # customer_id: int
    # first_name: Optional[str]
    # last_name: Optional[str]
    first_name: str
    last_name: str
    email: str
    phone_number: str

class LoginM(BaseModel):
    email: str
    phone_number: str 

class OrdersM(BaseModel):
    # order_id: int
    customer_id: int
    order_date: date
    total_amount: float

class OrderDetailsM(BaseModel):
    # order_detail_id: int
    order_id: int
    song_id: int
    quantity: int
    price: float

class EmployeesM(BaseModel):
    # employee_id: int
    first_name: str
    last_name: str
    hire_date: date
    position: str

class PublishersM(BaseModel):
    # publisher_id: int
    name: str
    country: str

class CopyrightsM(BaseModel):
    # copyright_id: int
    song_id: int
    publisher_id: int
    royalty_rate: float