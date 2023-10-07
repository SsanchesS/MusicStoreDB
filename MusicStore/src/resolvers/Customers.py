from sql_base.base import base_worker
from sql_base.models import CustomersM

def get_Customer(customer_id) -> str:
    get_customer = base_worker.insert_data(f"SELECT * FROM Customers WHERE customer_id = {customer_id}",())
    return get_customer

def new_Customer(customer: CustomersM) -> str:
    new_customer_id = base_worker.insert_data(f"""
        INSERT INTO Customers (first_name, last_name, email, phone_number) 
        VALUES (?, ?, ?, ?) RETURNING customer_id;
    """, (customer.first_name, customer.last_name, customer.email, customer.phone_number))
    return new_customer_id

def upd_Customer(customer_id, customer: CustomersM) -> str:
    upd_customer_id = base_worker.insert_data(f"""
        UPDATE Customers 
        SET first_name = ?, last_name = ?, email = ?, phone_number = ?
        WHERE customer_id = {customer_id} 
        RETURNING customer_id;
    """, (customer.first_name, customer.last_name, customer.email, customer.phone_number))
    return upd_customer_id

def del_Customer(customer_id) -> str:
    del_customer_id = base_worker.insert_data(f"DELETE FROM Customers WHERE customer_id = {customer_id} RETURNING customer_id;",())
    return del_customer_id