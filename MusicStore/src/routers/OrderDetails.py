from fastapi import APIRouter, HTTPException
from sql_base.models import OrderDetailsM
import resolvers.OrderDetails

OrderDetails_router = APIRouter()

@OrderDetails_router.get('/{order_detail_id}')
def get_OrderDetail(order_detail_id: int):
    order_detail = resolvers.OrderDetails.get_OrderDetail(order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail=f"OrderDetail with id {order_detail_id} not found")
    return {"OrderDetail": order_detail}

@OrderDetails_router.post('/')
def new_OrderDetail(order_detail: OrderDetailsM):
    new_id = resolvers.OrderDetails.new_OrderDetail(order_detail)
    return {"code": 201, "id": new_id}

@OrderDetails_router.put('/{order_detail_id}')
def update_OrderDetail(order_detail_id: int, order_detail: OrderDetailsM):
    upd_id = resolvers.OrderDetails.upd_OrderDetail(order_detail_id, order_detail)
    if upd_id is None:
        raise HTTPException(status_code=404, detail=f"OrderDetail with id {order_detail_id} not found")
    return {"Update OrderDetail": upd_id}

@OrderDetails_router.delete('/{order_detail_id}')
def delete_OrderDetail(order_detail_id: int):
    del_id = resolvers.OrderDetails.del_OrderDetail(order_detail_id)
    if del_id is None:
        raise HTTPException(status_code=404, detail=f"OrderDetail with id {order_detail_id} not found")
    return {"Delete OrderDetail": del_id}