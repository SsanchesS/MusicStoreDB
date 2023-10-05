from sql_base.base import base_worker
from sql_base.models import OrderDetailsM

def get_OrderDetail(OrderDetail_id) -> int:
    get_OrderDetail1 = base_worker.insert_data(f"SELECT * FROM OrderDetail WHERE id = {OrderDetail_id}",())
    return get_OrderDetail1

def new_OrderDetail(OrderDetail: OrderDetailsM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO OrderDetail (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (OrderDetail.left_in_stock, OrderDetail.note))
    return new_id
# 
def upd_OrderDetail(OrderDetail_id,OrderDetail: OrderDetailsM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE OrderDetail SET left_in_stock=(?), note=(?) WHERE id = {OrderDetail_id} RETURNING id;""",
                                     (OrderDetail.left_in_stock, OrderDetail.note))
    return upd_id

def del_OrderDetail(OrderDetail_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM OrderDetail WHERE id = {OrderDetail_id} RETURNING id;",())
    return del_id