from sql_base.base import base_worker
from sql_base.models import OrdersM

def get_Order(Order_id) -> int:
    get_Order1 = base_worker.insert_data(f"SELECT * FROM Order WHERE id = {Order_id}",())
    return get_Order1

def new_Order(Order: OrdersM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Order (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Order.left_in_stock, Order.note))
    return new_id
# 
def upd_Order(Order_id,Order: OrdersM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Order SET left_in_stock=(?), note=(?) WHERE id = {Order_id} RETURNING id;""",
                                     (Order.left_in_stock, Order.note))
    return upd_id

def del_Order(Order_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Order WHERE id = {Order_id} RETURNING id;",())
    return del_id