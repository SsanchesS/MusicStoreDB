from fastapi import APIRouter
from sql_base.models import OrdersM
import resolvers.Orders

Orders_router = APIRouter()

@Orders_router.get('/')
def get_Order():
    return f'Response: {{text: Страница со списком Orders}}'

@Orders_router.get('/{Order_id}')
def get_Order(Order_id: int):
    get_Order1 = resolvers.Orders.get_Order(Order_id)
    return f'Order: {get_Order1}'

@Orders_router.post('/')
def new_Order(Order: OrdersM):
    new_id = resolvers.Orders.new_Order(Order)
    return f'{{code: 201, id: {new_id}}}'

@Orders_router.put('/{Order_id}')
def update_Order(Order_id:int,Order: OrdersM):
    upd_id = resolvers.Orders.upd_Order(Order_id,Order)
    return f'Update Order {upd_id}'

@Orders_router.delete('/{Order_id}')
def delelte_Order(Order_id: int):
    del_id = resolvers.Orders.del_Order(Order_id)
    return f'Delete Order {del_id}'