from sql_base.models import CustomersM 
from sql_base.base import base_worker

def check_login_request(сustomers: CustomersM):
    customer_id = base_worker.insert_data(f"SELECT customer_id FROM Customers WHERE email = ? AND phone_number = ?",(сustomers.email,сustomers.phone_number))
    return customer_id