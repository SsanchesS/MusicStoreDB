from sql_base.base import base_worker
from sql_base.models import CustomersM

def get_Customers(Customer_id) -> int:
    get_Customer = base_worker.insert_data(f"SELECT * FROM Customer WHERE id = {Customer_id}",())
    return get_Customer

def new_Customer(Customer: CustomersM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Customer (Customername, password, card) 
                                    VALUES(?,?,?) RETURNING id;""",
                                    (Customer.Customername, Customer.password, Customer.card))
    return new_id
# 
def upd_Customer(Customer_id,Customer: CustomersM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Customer SET Customername=(?), password=(?), card=(?) WHERE id = {Customer_id} RETURNING id;""",
                                     (Customer.Customername, Customer.password, Customer.card))
    return upd_id

def del_Customer(Customer_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Customer WHERE id = {Customer_id} RETURNING id;",())
    return del_id