from fastapi import APIRouter
from sql_base.models import OrdersM
import resolvers.Orders

Orders_router = APIRouter()

@Orders_router.get('/{order_id}')
def get_Order(order_id: int):
    order = resolvers.Orders.get_Order(order_id)
    if order is None:
        return {"code": 404, 'message': f"Order with id {order_id} not found"}
    return {"code": 201, "Order": order}

@Orders_router.post('/')
def new_Order(order: OrdersM):
    new_id = resolvers.Orders.new_Order(order)
    return {"code": 201, "id": new_id}

@Orders_router.put('/{order_id}')
def update_Order(order_id: int, order: OrdersM):
    upd_id = resolvers.Orders.upd_Order(order_id, order)
    if upd_id is None:
        return {"code": 404, 'message': f"Order with id {order_id} not found"}
    return {"code": 201, "Update Order": upd_id}

@Orders_router.delete('/{order_id}')
def delete_Order(order_id: int):
    del_id = resolvers.Orders.del_Order(order_id)
    if del_id is None:
        return {"code": 404, 'message': f"Order with id {order_id} not found"}
    return {"code": 201, "Delete Order": del_id}