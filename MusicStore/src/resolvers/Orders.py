from sql_base.base import base_worker
from sql_base.models import OrdersM

def get_Order(order_id) -> str:
    get_order = base_worker.insert_data(f"SELECT * FROM Orders WHERE order_id = {order_id}",())
    return get_order

def new_Order(order: OrdersM) -> str:
    new_order_id = base_worker.insert_data(f"""
        INSERT INTO Orders (customer_id, order_date, total_amount) 
        VALUES (?, ?, ?) RETURNING order_id;
    """, (order.customer_id, order.order_date, order.total_amount))
    return new_order_id

def upd_Order(order_id, order: OrdersM) -> str:
    upd_order_id = base_worker.insert_data(f"""
        UPDATE Orders 
        SET customer_id = ?, order_date = ?, total_amount = ?
        WHERE order_id = {order_id} 
        RETURNING order_id;
    """, (order.customer_id, order.order_date, order.total_amount))
    return upd_order_id

def del_Order(order_id) -> str:
    del_order_id = base_worker.insert_data(f"DELETE FROM Orders WHERE order_id = {order_id} RETURNING order_id;",())
    return del_order_id