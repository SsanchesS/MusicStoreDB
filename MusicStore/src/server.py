from fastapi import FastAPI
import uvicorn

from routers.Albums import Albums_router
from routers.Copyrights import Copyrights_router
from routers.Artists import Artists_router
from routers.Genres import Genres_router
from routers.Songs import Songs_router
from routers.Customers import Customers_router
from routers.Orders import Orders_router
from routers.OrderDetails import OrderDetails_router
from routers.Employees import Employees_router
from routers.Publishers import Publishers_router

from routers.login import login_router

from sql_base.base import base_worker

#https://metanit.com/python/fastapi/2.3.php

BASE_PATH = 'MusicStore.db'
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    print("БД не существует")
    base_worker.create_base('../sql/base.sql')
else:
    print("БД существует")
    

app = FastAPI()

@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}
    
app.include_router(Albums_router, prefix='/albums')
app.include_router(Copyrights_router, prefix='/copyrights')
app.include_router(Artists_router, prefix='/artists')
app.include_router(Genres_router, prefix='/genres')
app.include_router(Songs_router, prefix='/songs')
app.include_router(Customers_router, prefix='/customers')
app.include_router(Orders_router, prefix='/orders')
app.include_router(OrderDetails_router, prefix='/orderDetails')
app.include_router(Employees_router, prefix='/employees') 
app.include_router(Publishers_router, prefix='/publishers') 

app.include_router(login_router, prefix='/login')

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, host="127.0.0.1", reload=True)