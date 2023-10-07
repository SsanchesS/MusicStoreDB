from sql_base.base import base_worker
from sql_base.models import OrderDetailsM

def get_OrderDetail(order_detail_id) -> str:
    get_order_detail = base_worker.insert_data(f"SELECT * FROM OrderDetails WHERE order_detail_id = {order_detail_id}",())
    return get_order_detail

def new_OrderDetail(order_detail: OrderDetailsM) -> str:
    new_order_detail_id = base_worker.insert_data(f"""
        INSERT INTO OrderDetails (order_id, song_id, quantity, price) 
        VALUES (?, ?, ?, ?) RETURNING order_detail_id;
    """, (order_detail.order_id, order_detail.song_id, order_detail.quantity, order_detail.price))
    return new_order_detail_id

def upd_OrderDetail(order_detail_id, order_detail: OrderDetailsM) -> str:
    upd_order_detail_id = base_worker.insert_data(f"""
        UPDATE OrderDetails 
        SET order_id = ?, song_id = ?, quantity = ?, price = ?
        WHERE order_detail_id = {order_detail_id} 
        RETURNING order_detail_id;
    """, (order_detail.order_id, order_detail.song_id, order_detail.quantity, order_detail.price))
    return upd_order_detail_id

def del_OrderDetail(order_detail_id) -> str:
    del_order_detail_id = base_worker.insert_data(f"DELETE FROM OrderDetails WHERE order_detail_id = {order_detail_id} RETURNING order_detail_id;",())
    return del_order_detail_id