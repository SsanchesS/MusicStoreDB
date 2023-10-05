from fastapi import APIRouter
from sql_base.models import OrderDetailsM
import resolvers.OrderDetails

OrderDetails_router = APIRouter()

@OrderDetails_router.get('/')
def get_OrderDetail():
    return f'Response: {{text: Страница со списком OrderDetails}}'

@OrderDetails_router.get('/{OrderDetail_id}')
def get_OrderDetail(OrderDetail_id: int):
    get_OrderDetail1 = resolvers.OrderDetails.get_OrderDetail(OrderDetail_id)
    return f'OrderDetail: {get_OrderDetail1}'

@OrderDetails_router.post('/')
def new_OrderDetail(OrderDetail: OrderDetailsM):
    new_id = resolvers.OrderDetails.new_OrderDetail(OrderDetail)
    return f'{{code: 201, id: {new_id}}}'

@OrderDetails_router.put('/{OrderDetail_id}')
def update_OrderDetail(OrderDetail_id:int,OrderDetail: OrderDetailsM):
    upd_id = resolvers.OrderDetails.upd_OrderDetail(OrderDetail_id,OrderDetail)
    return f'Update OrderDetail {upd_id}'

@OrderDetails_router.delete('/{OrderDetail_id}')
def delelte_OrderDetail(OrderDetail_id: int):
    del_id = resolvers.OrderDetails.del_OrderDetail(OrderDetail_id)
    return f'Delete OrderDetail {del_id}'